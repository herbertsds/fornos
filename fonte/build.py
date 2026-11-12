"""Gera o site estático em dist/ a partir de data.py + vtex.json + extras.json.

Uso:
  python3 build.py                 # todas as fotos (sem limite), remove quase-duplicadas
  python3 build.py --max-fotos 6   # limita fotos por modelo (o artefato do Claude aceita só 512 arquivos)
  python3 build.py --keys m_frn48 b_bfe43   # só alguns modelos (teste)
Antes, para atualizar preços/fotos das lojas: python3 fetch.py   (grava vtex.json)
"""
import argparse, io, json, os, re, shutil, subprocess
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import data

ap = argparse.ArgumentParser()
ap.add_argument("--max-fotos", type=int, default=0)
ap.add_argument("--keys", nargs="*")
ap.add_argument("--out", default="dist")
a = ap.parse_args()

HERE = os.path.dirname(os.path.abspath(__file__))
vtex = json.load(open(os.path.join(HERE, "vtex.json")))
extras = json.load(open(os.path.join(HERE, "extras.json")))
keys = a.keys or list(data.M)
out = os.path.join(HERE, a.out)
shutil.rmtree(out, ignore_errors=True); os.makedirs(os.path.join(out, "i"))

def dl(job):
    k, j, u = job
    u = re.sub(r"/arquivos/ids/(\d+)/", r"/arquivos/ids/\1-800-800/", u)  # VTEX redimensiona pela URL
    r = subprocess.run(["curl", "-s", "--max-time", "40", u], capture_output=True)
    try:
        im = Image.open(io.BytesIO(r.stdout)).convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255)); bg.paste(im, mask=im.split()[3])
        g = bg.convert("L").resize((16, 16)); px = list(g.getdata()); avg = sum(px) / len(px)
        h = "".join("1" if p > avg else "0" for p in px)  # hash médio p/ achar fotos repetidas
        bg.thumbnail((800, 800)); buf = io.BytesIO(); bg.save(buf, "WEBP", quality=72)
        return k, j, h, buf.getvalue()
    except Exception:
        return k, j, None, None

jobs = [(k, j, u) for k in keys for j, u in enumerate(vtex.get(k, {}).get("images", []))]
res = list(ThreadPoolExecutor(16).map(dl, jobs))
by = {}
for k, j, h, b in res:
    if b: by.setdefault(k, []).append((j, h, b))
imgs, n = {}, 0
for k in keys:
    kept = []
    for j, h, b in sorted(by.get(k, []), key=lambda t: t[0]):
        if any(sum(x != y for x, y in zip(h, h2)) <= 12 for h2, _ in kept): continue
        kept.append((h, b))
        if a.max_fotos and len(kept) >= a.max_fotos: break
    ids = []
    for h, b in kept:
        n += 1; open(os.path.join(out, "i", f"{n}.webp"), "wb").write(b); ids.append(n)
    imgs[k] = ids

BAD = re.compile(r"\+ |liquidificador|\bkit\b|combo|torre", re.I)
models = {}
for k in keys:
    brand, model, L, dims, idims, typ, mount, note, q, must = data.M[k]
    offers = [o for o in vtex.get(k, {}).get("offers", []) if not BAD.search(o.get("name") or "")]
    m = dict(b=brand, m=model, l=L, d=dims, i=idims, t=typ, mt=mount, n=note, img=imgs.get(k, []),
             o=[[o["store"], o["name"], o["price"], o["link"]] for o in offers],
             q=f"forno {brand} {model.split('/')[0].split('(')[0].strip()}", x={})
    m.update(extras.get(k, {}))
    models[k] = m
spaces = [dict(id=s["id"], name=s["name"], d=s["dims"], fit=[x for x in s["fit"] if x in models],
               over=[x for x in s["over"] if x in models]) for s in data.SPACES]
site = {"models": models, "spaces": spaces}
json.dump(site, open(os.path.join(out, "site.json"), "w"), ensure_ascii=False, separators=(",", ":"))
t = open(os.path.join(HERE, "template.html")).read()
open(os.path.join(out, "index.html"), "w").write(
    t.replace("__DATA__", json.dumps(site, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")))
print(f"{len(models)} modelos, {n} fotos em {out}/")
