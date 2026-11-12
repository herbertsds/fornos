import json, subprocess, urllib.parse, re, unicodedata
def norm(s): return unicodedata.normalize("NFKD", s.lower()).encode("ascii","ignore").decode()
def get(h,q,f=0):
    r=subprocess.run(["curl","-s","--max-time","25",f"https://{h}/api/catalog_system/pub/products/search?ft={urllib.parse.quote(q)}&_from={f}&_to={f+49}"],capture_output=True)
    try: return json.loads(r.stdout)
    except: return []
SRC={"Dako":["www.dako.com.br"],"Cadence":["www.cadence.com.br"],"Continental":["www.continentalbrasil.com.br"],
     "Tramontina":["site.fastshop.com.br","www.webcontinental.com.br","www.lojasmm.com","www.colombo.com.br"],
     "Layr":["site.fastshop.com.br","www.webcontinental.com.br","www.lojasmm.com"]}
GENERIC=["site.fastshop.com.br","www.webcontinental.com.br","www.lojasmm.com"]
BAD=r"^(manipulo|garantia|grelha|assadeira|resistencia|termostato|kit|combo|cooktop|fogao|porta|puxador|botao|lampada|bandeja|tampa|queimador|registro|mangueira|coifa|depurador|micro)"
out={}
for b,hosts in SRC.items():
    for h in dict.fromkeys(hosts+GENERIC):
        for q in [f"forno {b}", f"{b} forno eletrico", f"{b} forno gas"]:
            for f in (0,50):
                res=get(h,q,f)
                if not isinstance(res,list) or not res: break
                for p in res:
                    n=norm(p.get("productName",""))
                    if norm(b) not in n or "forno" not in n or re.search(BAD,n): continue
                    if "fryer" in n and "forno" not in n: continue
                    specs={}
                    for k in p.get("allSpecifications",[]) or []:
                        if re.search(r"(dimens|altura|largura|profund|capacidade|litro|volume|interna|nicho|tipo|alimenta|funcionamento|instala)",norm(k)):
                            specs[k]=p.get(k)
                    it=p["items"][0] if p.get("items") else {}
                    price=None
                    for i in p.get("items",[]):
                        for s in i.get("sellers",[]):
                            co=s.get("commertialOffer",{})
                            if co.get("AvailableQuantity",0)>0 and co.get("Price",0)>150: price=co["Price"] if price is None else min(price,co["Price"])
                    key=(b,p.get("productReference") or p["productName"])
                    e=out.setdefault(p["productName"],{"brand":b,"ref":p.get("productReference"),"specs":specs,"offers":[],"images":[]})
                    if not e["specs"] and specs: e["specs"]=specs
                    e["offers"].append([h,price,p.get("link")])
                    if not e["images"]: e["images"]=[im["imageUrl"].split("?")[0] for im in it.get("images",[])][:8]
json.dump(out,open("newbrands.json","w"),ensure_ascii=False,indent=1)
for n,e in out.items():
    print(e["brand"],"|",n[:80],"|",e["ref"],"|",json.dumps(e["specs"],ensure_ascii=False)[:300])
