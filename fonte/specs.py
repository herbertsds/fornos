import json, subprocess, urllib.parse, re, unicodedata, sys
def norm(s): return unicodedata.normalize("NFKD", s.lower()).encode("ascii","ignore").decode()
def get(h,q):
    r=subprocess.run(["curl","-s","--max-time","25",f"https://{h}/api/catalog_system/pub/products/search?ft={urllib.parse.quote(q)}&_from=0&_to=49"],capture_output=True)
    try: return json.loads(r.stdout)
    except: return []
for h,q,flt in [(a.split("|")[0],a.split("|")[1],a.split("|")[2]) for a in sys.argv[1:]]:
    for p in get(h,q) or []:
        n=p["productName"]
        if not re.search(flt,norm(n)): continue
        sp={k:p.get(k) for k in (p.get("allSpecifications") or []) if re.search(r"(dimens|altura|largura|profund|nicho|intern|capacidade|volume|litro|gas|aliment|tipo de forno|instala)",norm(k)) and "embalag" not in norm(k)}
        pr=[s["commertialOffer"]["Price"] for i in p.get("items",[]) for s in i.get("sellers",[]) if s["commertialOffer"].get("AvailableQuantity",0)>0]
        print("##",h,"|",n[:90],"| R$",min(pr) if pr else None,"| imgs",len(p["items"][0]["images"]) if p.get("items") else 0)
        print("  ",json.dumps(sp,ensure_ascii=False)[:600])
