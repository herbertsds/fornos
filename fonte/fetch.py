import re, json, subprocess, urllib.parse, unicodedata, sys, os
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(__file__))
from data import M, BRAND_STORE, GENERIC

STORE_NAME = {"www.mondial.com.br":"Loja Mondial","www.philco.com.br":"Loja Philco","www.britania.com.br":"Loja Britânia",
 "loja.electrolux.com.br":"Loja Electrolux","www.brastemp.com.br":"Loja Brastemp","www.consul.com.br":"Loja Consul",
 "www.oster.com.br":"Loja Oster","www.midea.com.br":"Loja Midea","www.elgin.com.br":"Loja Elgin","www.arno.com.br":"Loja Arno",
 "site.fastshop.com.br":"Fast Shop","www.webcontinental.com.br":"Webcontinental","www.lojasmm.com":"Lojas MM","www.dako.com.br":"Loja Dako","www.continentalbrasil.com.br":"Loja Continental"}

def norm(s):
    return unicodedata.normalize("NFKD", s.lower()).encode("ascii","ignore").decode()

def get(url):
    r = subprocess.run(["curl","-s","--max-time","25",url],capture_output=True)
    try: return json.loads(r.stdout.decode("utf-8","ignore"))
    except Exception: return []

def search(host, q):
    return get(f"https://{host}/api/catalog_system/pub/products/search?ft={urllib.parse.quote(q)}&_from=0&_to=19") or []

BAD = r"(^(garantia|grelha|assadeira|resistencia|termostato|interruptor|kit|combo|torre|bandeja|pedra|forma|puxador|lampada|botao|porta|suporte|pe |cooktop|fogao|servico|instalacao))|garantia estendida"
OV = {
 "f_top50":(["fogatti top 50"],[r"fogatti",r"top ?50"],[]),
 "f_top60":(None,[r"fogatti",r"top ?60"],[r"smart"]),
 "f_top70":(None,[r"fogatti",r"70"],[]),
 "n_top70":(None,[r"nardelli",r"70"],[]),
 "n_top60":(None,[r"nardelli",r"top ?60"],[r"smart"]),
 "s_fe50":(None,[r"suggar",r"50"],[r"embutir"]),
 "s_fe60":(None,[r"suggar",r"60"],[r"embutir"]),
 "s_fe09":(["suggar forno 9 litros","suggar fe09"],[r"suggar",r"(fe09|\b9 ?l)"],[]),
 "o_ofor160":(None,[r"15 ?l"],[]),
 "o_10l":(["oster compact"],[r"compact"],[r"25 ?l"]),
 "o_22":(None,[r"22 ?l"],[]),
 "o_45":(None,[r"45 ?l"],[]),
 "m_52":(["grand family 52","FRN-52-B"],[r"52",r"grand"],[]),
 "m_fr42":(["family ii 42","FRN-42-B"],[r"42",r"family ii"],[r"grill"]),
 "mu_50":(None,[r"mueller",r"50"],[r"embutir"]),
 "fi_grill44":(None,[r"fischer",r"44"],[r"gourmet"]),
 "a_for1":(["arno forno turbo"],[r"arno",r"forno"],[]),
 "e_for090":(["elgin forno 9"],[r"(for0?90|\b9 ?l)"],[r"fryer|fritadeira"]),
 "v_giii50":(["venax totale","venax cristallo","venax forno embutir"],[r"venax",r"(totale|cristallo|g ?iii)"],[]),
 "fi_inf50":(None,[r"infinity",r"50"],[]),
 "p_pfe50pe":(["philco pfe50","philco 50l full glass","philco forno 50l"],[r"philco",r"(pfe50|full glass)"],[]),
 "p_pfe48p":(["philco pfe48","philco pfe46","philco 46l"],[r"philco",r"(pfe48|pfe46)"],[]),
 "o_ofor310":(["oster 30l","oster forno 30"],[r"oster",r"30 ?l"],[]),
 "m_fr20":(["master cooker","FR-20"],[r"(master cooker|fr-20)"],[]),
 "bd_to1745":(["black decker 4 fatias","TO1745"],[r"(to1745|4 fatias)"],[]),
 "bd_to3250":(["TO3250","black decker forno 8"],[r"to3250"],[]),
 "p_pfe70i":(["philco 70l","philco pfe70"],[r"philco",r"(pfe70|70 ?l)"],[]),
 "el_fb54x":(["electrolux forno bancada","FB54X","electrolux 44l"],[r"electrolux",r"(fb54|44 ?l)"],[r"embutir"]),
 "v_ind77":(["venax industrial 77","forno industrial 77l"],[r"77"],[]),
 "n_cal45":(None,[r"nardelli",r"calabria"],[]),
}
OV.update({
 "n_top70":(None,[r"nardelli",r"top ?70"],[]),
 "f_top70":(["fogatti top 70"],[r"fogatti",r"top ?70"],[]),
 "s_fe60":(None,[r"suggar",r"(fe60|60 ?l)"],[r"embutir"]),
 "s_fe50":(None,[r"suggar",r"(fe50|50 ?l)"],[r"embutir"]),
 "mu_50":(None,[r"mueller",r"(mfb50|50 ?l)"],[r"embutir"]),
 "fi_grill44":(None,[r"fischer",r"grill",r"44"],[r"gourmet|embutir|premier"]),
 "fi_inf50":(["fischer infinity gas 50"],[r"infinity",r"gas",r"50"],[r"eletrico"]),
 "o_10l":(["oster compact"],[r"forno",r"compact"],[r"fritadeira|fryer"]),
 "o_ofor160":(None,[r"(ofor160|15 ?l)"],[]),
 "f_i25":(["fogatti i25","black i25"],[r"i25"],[]),
 "b_bfe35":(["BFE35","britania 35l"],[r"(bfe35|35 ?l)"],[]),
 "b_bfe11":(["BFE11","britania 10l"],[r"(bfe11|10 ?l)"],[r"bfe10v"]),
})
OV.update({
 "ct_bc44":(["continental bancada 44","BC44B"],[r"continental",r"44"],[r"embutir"]),
 "sa_nv76":(["samsung forno embutir","NV7B4420","NV7B4545"],[r"samsung",r"76"],[]),
 "ph_ai551":(["philips walita forno ai551","airfryer forno philips"],[r"(ai551|airfryer forno)"],[]),
 "d_emb52":(None,[r"dako",r"embutir",r"52"],[r"torre|cooktop"]),
 "d_emb80":(None,[r"dako",r"embutir",r"80"],[r"select|diplomata"]),
})
OV.update({"b_bfe49":(None,[r"bfe49\b"],[r"embutir|bfe49p"]),"b_bfe49pe":(["BFE49P","britania embutir 47"],[r"britania",r"embutir",r"(bfe49p|47 ?l)"],[r"bfe47"])})
STRICT = set(OV)

def one(key):
    brand, model, L, dims, idims, typ, mount, note, q, must = M[key]
    qs, rx, nots = OV.get(key,(None,None,[]))
    qs = qs or [q]
    rx = rx or [re.escape(norm(t)) for t in must]
    hosts = ([BRAND_STORE[brand]] if brand in BRAND_STORE else []) + GENERIC
    offers, images, seen, done = [], [], set(), set()
    for h in hosts:
        for qq in qs:
            res = search(h, qq)
            if not isinstance(res, list): continue
            for p in res:
                name = norm(p.get("productName",""))
                if p.get("productId") in done: continue
                if re.search(BAD,name) or not ("forno" in name or "fryer" in name): continue
                if not all(re.search(r,name) for r in rx) or any(re.search(r,name) for r in nots): continue
                if h in GENERIC and key not in STRICT and norm(brand.split("+")[0]) not in name: continue
                if h in GENERIC and key in STRICT and norm(brand.split("+")[0]) not in name and len(rx)<2: continue
                done.add(p.get("productId"))
                price = None
                for it in p.get("items",[]):
                    for s in it.get("sellers",[]):
                        co = s.get("commertialOffer",{})
                        if co.get("AvailableQuantity",0) > 0 and co.get("Price",0) > 150:
                            price = co["Price"] if price is None else min(price, co["Price"])
                    for im in it.get("images",[]):
                        iid = im.get("imageId")
                        if iid not in seen and len(images) < 60:
                            seen.add(iid); images.append(im["imageUrl"].split("?")[0])
                link = p.get("link") or f"https://{h}/{p.get('linkText')}/p"
                offers.append({"store":STORE_NAME[h],"name":p.get("productName"),"price":price,"link":link})
    return key, {"offers":offers,"images":images}

if __name__ == "__main__":
    keys = sys.argv[1:] or list(M)
    with ThreadPoolExecutor(8) as ex:
        out = dict(ex.map(one, keys))
    if sys.argv[1:]:
        old=json.load(open(os.path.join(os.path.dirname(__file__),"vtex.json"))); old.update(out); out=old
    json.dump(out, open(os.path.join(os.path.dirname(__file__),"vtex.json"),"w"), ensure_ascii=False, indent=1)
    for k,v in out.items():
        pr = [o["price"] for o in v["offers"] if o["price"]]
        print(f"{k:14} offers={len(v['offers']):2} priced={len(pr):2} imgs={len(v['images'])} {[o['name'][:45] for o in v['offers'][:2]]}")
