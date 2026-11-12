# key: brand, model, liters, (H,W,D), (iH,iW,iD) or None, type, mount, note, search query, must tokens
E, AF, G = "Elétrico", "Elétrico + air fryer", "Gás"
B, EM = "Bancada", "Embutir"
M = {
"p_pfe50pe": ("Philco","PFE50PE Full Glass",50,(35,60,42),None,E,B,"Altura exatamente no limite do espaço sob o cooktop","philco pfe50pe",["pfe50"]),
"f_top50": ("Fogatti","Top 50 Black",50,(33.7,57.5,45.1),None,E,B,"","fogatti top 50",["fogatti","50"]),
"f_top48": ("Fogatti","Top 48 Black",48,(33.7,57.5,45.1),(20.4,45,37.5),E,B,"Interior baixo (20 cm)","fogatti top 48",["fogatti","48"]),
"m_frn48": ("Mondial","Family Grill Inox FRN-48-BI",48,(34,55,35.65),None,E,B,"Luz interna e grill dourador","FRN-48-BI",["frn-48"]),
"p_pfe49p": ("Philco","PFE49P",46,(31.7,56,46.5),None,E,B,"","philco pfe49p",["pfe49"]),
"p_pfe48p": ("Philco","PFE46P / PFE48P / PFE48IPL",46,(31.6,55.5,44),None,E,B,"O PFE48IPL é autolimpante","philco pfe48",["pfe48","pfe46"]),
"o_45": ("Oster","OFOR454 / OFOR455 (45L Grafite)",45,(34.5,55.5,42),None,E,B,"Luz interna e convecção","oster 45l",["45"]),
"o_fd": ("Oster","French Door TSSTTVFDMAF",42,(32.5,55,49),None,AF,B,"Uma loja informa 37,5 × 51,2 × 60,5: confirmar","oster french door",["french door"]),
"m_fr42": ("Mondial","Family II FR-42 / FRN-42",42,(33.5,53,37.5),None,E,B,"","forno 42L family",["42l"]),
"s_fe42": ("Suggar","FE4201PT / FE4202PT",42,(32.6,51.3,39.25),(27.5,37.5,34),E,B,"","suggar forno 42",["suggar","42"]),
"n_top40": ("Nardelli","Top 40",40,(34.4,50,47.5),(28,37,39.5),E,B,"","nardelli top 40",["nardelli","40"]),
"f_top40": ("Fogatti","Top 40 Black",40,(34,50,47.5),(20,37,39.5),E,B,"Outra loja informa profundidade de 34 cm","fogatti top 40",["fogatti","40"]),
"p_pfe42p": ("Philco","PFE42P",38,(33.6,49.5,39.5),None,E,B,"","philco pfe42p",["pfe42"]),
"b_bfe40p": ("Britânia","BFE40P",36,(32.9,51.8,38),None,E,B,"","BFE40P",["bfe40"]),
"b_bfe35": ("Britânia","BFE35",35,(34.5,53.5,37),None,E,B,"","BFE35",["bfe35"]),
"o_ofor310": ("Oster","OFOR310",30,(30.8,50,38.8),None,E,B,"","oster forno 30l",["30"]),
"o_22": ("Oster","TSSTTV7022R (22L Red)",22,(31.5,50.4,42.6),None,E,B,"","oster 22l",["22"]),
"m_52": ("Mondial","Grand Family II FR-52 / FRN-52",52,(35.2,56,40.6),None,E,B,"Algumas lojas informam 35,5 × 57 × 41,5","FRN-52-B",["52"]),
"mu_50": ("Mueller","MFB50K / MFB50F",50,(35.5,58,52),(29.5,39,43.5),E,B,"","mueller forno 50",["mueller","50"]),
"fi_grill44": ("Fischer","Grill 44L",44,(36,57.7,50),(26.7,39.2,42.5),E,B,"Autolimpante","fischer grill 44",["fischer","44"]),
"s_fe50": ("Suggar","FE5011PT / FE5012PT",50,(36,56,43),(30.5,42,36.5),E,B,"","suggar forno 50",["suggar","50"]),
"p_pfe65": ("Philco","PFE65",65,(36.3,59.8,49.8),(21.3,43.4,44.1),E,B,"Uma loja informa P 45,3","philco pfe65",["pfe65"]),
"m_frn60": ("Mondial","Family Grill Inox FRN-60-BI",60,(36.6,61.4,36.8),None,E,B,"","FRN-60-BI",["frn-60"]),
"p_pfe60i": ("Philco","PFE60I",60,(37,59.8,42.3),None,E,B,"Outra loja informa 41,2 × 64,2 × 44,1","philco pfe60",["pfe60"]),
"s_fe60": ("Suggar","FE6011PT / FE60",60,(37.1,59.5,47.5),None,E,B,"Outra loja: 37,4 × 59,7 × 47,1","suggar forno 60",["suggar","60"]),
"p_pfe51p": ("Philco","PFE51P",50,(37.3,61,47.3),None,E,B,"","philco pfe51p",["pfe51"]),
"fi_gg44": ("Fischer","Gourmet Grill 44L",44,(37,57.5,52),(26.7,39.2,42.5),E,B,"Autolimpante, até 320 °C","fischer gourmet grill",["fischer","gourmet"]),
"fi_premier48": ("Fischer","Premier 48L",48,(37,57.5,52.4),(27.5,39.2,44.5),E,B,"","fischer premier",["fischer","premier"]),
"n_s45": ("Nardelli","S45 Black",45,(33.5,50,50.8),(21,37,43),E,B,"","nardelli s45",["nardelli","45"]),
"m_afo25": ("Mondial","Air Fryer Forno Oven AFO-25L-BI",25,(36.5,45,41),None,AF,B,"Outra loja informa 37 × 41 × 45","AFO-25L",["afo-25"]),
"m_fr20": ("Mondial","Master Cooker FR-20",10,(23,38,28),None,E,B,"Bandeja de 24 × 24 cm","FR-20",["fr-20"]),
"b_bfe11": ("Britânia","BFE11",10,(19.8,35.4,28),None,E,B,"Duas resistências","BFE11",["bfe11"]),
"b_bfe10v": ("Britânia","BFE10V",10,(19.4,35.4,27.1),None,E,B,"Medidas de comparadores: confirmar","BFE10",["bfe10"]),
"a_for1": ("Arno","Turbo Quartzo FOR1",10,(24.4,30,24.4),None,E,B,"","forno arno",["forno"]),
"bd_ft9n": ("Black+Decker","FT9N",9,(20.3,36.6,26.5),None,E,B,"Profundidade assumida (26,5): confirmar","black decker forno ft9",["ft9"]),
"e_for090": ("Elgin","FOR090",9,(29,37,22),None,E,B,"","elgin forno",["forno"]),
"s_fe09": ("Suggar","FE09",9,(27.7,36.8,20.2),None,E,B,"","suggar forno 9",["suggar"]),
"m_fr09": ("Mondial","Pratic Cook FR-09",6,(20,35,18),None,E,B,"Outra fonte: 24 × 39,5 × 21,5","FR-09",["fr-09"]),
"bd_to1745": ("Black+Decker","TO1745SSG (4 fatias)",4.6,(23,42.9,29.5),None,E,B,"Pequeno demais em litros; só por referência","black decker to1745",["to1745"]),
"bd_ft9": ("Black+Decker","FT9 Bake Chef Mini",9,(24,41,29),None,E,B,"Buscapé lista 24 × 29 × 41: confirmar","black decker ft9",["ft9"]),
"o_10l": ("Oster","Compact 10L TSSTTV10LTR",10,(20,36,31),None,E,B,"Outra fonte: 36 × 20 × 31","oster 10l",["10"]),
"o_ofor160": ("Oster","Forno e Fryer Compact OFOR160",15,(34.5,34.5,31),None,AF,B,"","oster ofor160",["15"]),
"m_afon12": ("Mondial","Air Fryer Oven AFON-12L",12,(36,36.1,32),None,AF,B,"Outra loja informa 39 × 32 × 36,1","AFON-12L",["12l"]),
"o_18": ("Oster","Convection Cook 18L",18,(24.8,42.2,32),None,E,B,"","oster 18l",["18"]),
"o_ofor250": ("Oster","Forno e Fryer OFOR250",25,(36,40,37),None,AF,B,"","oster ofor250",["25"]),
"f_i25": ("Fogatti","Black i25",25,(29.3,43.3,37.5),(24.3,31.3,31.3),E,B,"","fogatti i25",["fogatti","25"]),
"bd_to3250": ("Black+Decker","TO3250XSB",8,(29.2,55.9,36.8),None,E,B,"Aceita forma de 23 × 33 cm","black decker to3250",["to3250"]),
"m_afdo25": ("Mondial","French Door AFDO-25L",25,(39.5,40,40),None,AF,B,"","AFDO-25L",["afdo"]),
"p_pfe70i": ("Philco","PFE70I Inox",70,(39,63.7,46.5),None,E,B,"","philco pfe70",["pfe70"]),
"s_fe66": ("Suggar","FE6601PT / FE6602PT",66,(39.6,63.5,44.5),(34.3,49.7,38),E,B,"Maior interior da lista","suggar forno 66",["suggar","66"]),
"n_top60": ("Nardelli","Top 60 Black",60,(41.5,57.5,45.2),(28,45,37.5),E,B,"Algumas lojas dão altura interna de 35,3","nardelli top 60",["nardelli","60"]),
"n_smart60": ("Nardelli","Smart 60 (espeto giratório)",60,(41.5,57.5,45.2),(28,45,37.5),E,B,"","nardelli smart 60",["nardelli","smart"]),
"f_top60": ("Fogatti","Top 60",60,(41.3,57.6,45.2),(27,45,37.7),E,B,"","fogatti top 60",["fogatti","60"]),
"f_smart60s": ("Fogatti","Smart 60S (espeto giratório)",60,(41.3,57.6,45.2),(27,45,37.7),E,B,"","fogatti smart",["fogatti","smart"]),
"t_top60": ("Terim","Top 60 Black",60,(41.5,57.5,45.2),(28,45,None),E,B,"","terim forno 60",["terim"]),
"best60": ("Best","60 Litros Plus",60,(42.5,62.5,45),None,E,B,"","forno best 60",["best"]),
"el_fb54x": ("Electrolux","FB54X (bancada 44L Inox)",44,(47.9,53.5,43.1),None,E,B,"Pode estar fora de linha","FB54X",["fb54"]),
"mi_tsd62": ("Midea","TSD62 (Air Fryer) / TSM62",68,(59.5,59.5,42.1),None,AF,EM,"O corpo cabe, mas o fabricante pede nicho de 59 × 56,8 × 57,5. Só 220 V","forno embutir 68L",["68"]),
"el_oe60m": ("Electrolux","OE60M",59,(59.8,59.7,47.8),None,E,EM,"O corpo cabe; nicho pedido 58,3 × 56 × 55. Pode estar fora de linha","OE60M",["oe60"]),
"b_bfe50p": ("Britânia","BFE50P",50,(50,70,50),None,E,B,"","BFE50P",["bfe50"]),
"n_top70": ("Nardelli","Top 70",70,(41.5,57.5,52.5),(28,45,37.5),E,B,"","nardelli top 70",["nardelli","70"]),
"f_top70": ("Fogatti","Top 70 Black",70,(41.5,57.5,52.5),(28,45,37.5),E,B,"","fogatti top 70",["fogatti","70"]),
"n_cal45": ("Nardelli","Calabria 45",45,(33.8,57.5,55.5),(26,37.2,46),E,B,"","nardelli calabria",["calabria"]),
"el_me4ep": ("Electrolux","ME4EP (forno + micro-ondas)",43,(45.5,59.5,56.7),None,E,EM,"Forno combinado com micro-ondas","ME4EP",["me4"]),
"c_cob47": ("Consul","COB47BE",47,(46.5,60,58.4),None,E,EM,"Menor Consul achado; nenhum Consul cabe","COB47BE",["47"]),
"br_bob47": ("Brastemp","BOB47AE",47,(46.5,60,58.4),None,E,EM,"Menor Brastemp achado; nenhum Brastemp cabe","BOB47AE",["47"]),
"v_giii50": ("Venax","Totale Nero / Cristallo GIII 50L",51.8,(61,51.7,61.5),(29,37.8,47),G,EM,"Gás GLP","venax forno 50",["venax"]),
"fi_inf50": ("Fischer","Infinity 50L a gás com grill",50,(45,59.5,60.8),None,G,EM,"Nicho pedido 44 × 56 × 58. Sai de fábrica para GLP","fischer infinity",["infinity"]),
"br_boa84": ("Brastemp","BOA84AE 78L a gás",78,(62,60,58.4),None,G,EM,"Nicho pedido 61 × 57 × 58; convecção e grill","BOA84",["78"]),
"v_ind77": ("Venax","Industrial 77L de bancada a gás",77,(59.5,60.5,60.5),(33,50,46.8),G,B,"Forno industrial, GLP baixa pressão, acendimento manual","venax industrial 77",["77"]),
}
# space -> list of (key, status)
S1 = "p_pfe50pe f_top50 f_top48 m_frn48 p_pfe49p p_pfe48p o_45 o_fd m_fr42 s_fe42 n_top40 f_top40 p_pfe42p b_bfe40p b_bfe35 o_ofor310 o_22".split()
U1 = "m_52 mu_50 fi_grill44 s_fe50 p_pfe65 m_frn60 p_pfe60i s_fe60 p_pfe51p fi_gg44 fi_premier48 n_s45 m_afo25".split()
S2 = "m_fr20 b_bfe11 b_bfe10v a_for1 bd_ft9n e_for090 s_fe09 m_fr09".split()
U2 = "bd_to1745 bd_ft9 o_10l o_ofor160 m_afon12 o_18 o_ofor250 f_i25 bd_to3250 m_afdo25".split()
S3 = "p_pfe70i s_fe66 n_top60 n_smart60 f_top60 f_smart60s t_top60 best60 s_fe60 p_pfe60i m_frn60 m_52 p_pfe51p m_frn48 o_45 el_fb54x m_fr42 m_afo25".split()
U3 = "mi_tsd62 el_oe60m p_pfe65 b_bfe50p mu_50 fi_gg44 fi_premier48 n_top70 f_top70 n_cal45 el_me4ep c_cob47 br_bob47 v_giii50 fi_inf50 br_boa84 v_ind77 n_s45".split()
SPACES = [
 {"id":"cooktop","name":"Sob o cooktop","dims":(35,62,50),"fit":S1,"over":U1},
 {"id":"microondas","name":"Sobre o micro-ondas","dims":(43.5,57,29),"fit":S2,"over":U2},
 {"id":"airfryer","name":"Lugar da air fryer","dims":(71,67,48.5),"fit":S3,"over":U3},
]
BRAND_STORE = {"Mondial":"www.mondial.com.br","Philco":"www.philco.com.br","Britânia":"www.britania.com.br",
 "Electrolux":"loja.electrolux.com.br","Brastemp":"www.brastemp.com.br","Consul":"www.consul.com.br",
 "Oster":"www.oster.com.br","Midea":"www.midea.com.br","Elgin":"www.elgin.com.br","Arno":"www.arno.com.br"}
GENERIC = ["site.fastshop.com.br","www.webcontinental.com.br","www.lojasmm.com"]
M.update({
"d_prat70": ("Dako","Pratiko 70L (espeto giratório)",70,(41.5,62.2,45.6),None,E,B,"","dako pratiko 70",["pratiko","70"]),
"d_prat50": ("Dako","Pratiko 50L",50,(36.5,56.1,41.5),None,E,B,"","dako pratiko 50",["pratiko","50"]),
"d_sup44": ("Dako","Supreme 44L com grill",44,(36.1,58,52.3),None,E,B,"","dako supreme 44",["supreme","44"]),
"d_fryer15": ("Dako","Forno Fryer 15L",15,(34,34.5,31.5),None,AF,B,"","dako forno fryer 15",["fryer","15"]),
"d_emb52": ("Dako","Supreme 52L de embutir",52,(46,60,54.2),None,E,EM,"Nicho pedido 44,5 × 58,3 × 57","dako embutir 52",["embutir","52"]),
"d_emb80": ("Dako","Supreme 80L de embutir",80,(59.5,59.5,57.5),None,E,EM,"Nicho pedido 58,4 × 56 × 59,5","dako embutir 80",["embutir","80"]),
"ct_bc44": ("Continental","BC44B 44L com grill",44,(38.7,53.6,43),None,E,B,"","continental bancada 44",["44"]),
"ct_oc4em": ("Continental","OC4EM 50L de embutir",50,(45.6,59.6,57.5),None,E,EM,"Nicho pedido 45 × 56 × 53 (sobreposto ao móvel)","OC4EM",["oc4em"]),
"ct_oc4gm": ("Continental","OC4GM 50L a gás",50,(45.6,59.6,57.5),None,G,EM,"Nicho pedido 45 × 56 × 53 (sobreposto ao móvel)","OC4GM",["oc4gm"]),
"ct_oc8gm": ("Continental","OC8GM 80L a gás",80,(59.6,59.6,57.5),None,G,EM,"Nicho pedido 59 × 56 × 53 (sobreposto ao móvel)","OC8GM",["oc8gm"]),
"tr_smart22": ("Tramontina","Smart 22L by Breville",22,(28,47.5,41),None,E,B,"Convecção; outra loja informa 28 × 47 × 40","tramontina smart 22",["smart","22"]),
"sa_nv76": ("Samsung","NV7B4420XAK / NV7B4545SAK 76L",76,(59.6,59.5,57),None,AF,EM,"Nicho pedido 56 × 59,6 × 57; função air fry e Wi-Fi","samsung forno embutir 76",["76"]),
"ph_ai551": ("Philips Walita","Airfryer Forno Série 5000 AI551 12L",12,(34,37,37),None,AF,B,"Outra fonte informa 31,5 × 30,7 × 40,3","airfryer forno philips ai551",["ai551"]),
})
BRAND_STORE.update({"Dako":"www.dako.com.br","Continental":"www.continentalbrasil.com.br"})
S1 += ["tr_smart22"]; U1 += ["d_prat50","d_sup44","ct_bc44"]
U2 += ["d_fryer15","ph_ai551"]
S3 += ["d_prat70","d_prat50","ct_bc44"]; U3 += ["d_sup44","d_emb52","d_emb80","ct_oc4em","ct_oc4gm","ct_oc8gm","sa_nv76"]
for s in SPACES:
    s["fit"]={"cooktop":S1,"microondas":S2,"airfryer":S3}[s["id"]]; s["over"]={"cooktop":U1,"microondas":U2,"airfryer":U3}[s["id"]]
M.update({
"b_bfe43": ("Britânia","BFE43 43L",43,(34.8,54.5,41.5),None,E,B,"Ficha oficial; uma loja informa 34,6 × 54,1 × 39,5","BFE43",["bfe43"]),
"b_bfe44p": ("Britânia","BFE44P 44L",44,(34.6,54.1,39.5),None,E,B,"Ficha oficial","BFE44P",["bfe44"]),
"b_bfe41p": ("Britânia","BFE41P 36L",36,(33,53.5,37),None,E,B,"Ficha oficial","BFE41P",["bfe41"]),
"b_bfe49": ("Britânia","BFE49 49L",49,(37.3,61,47.3),None,E,B,"Ficha oficial","BFE49",["bfe49"]),
"b_bfe55p": ("Britânia","BFE55P 52L",52,(36.3,61,47.3),None,E,B,"Ficha oficial; uma loja informa 34,9 × 58,3 × 45,3","BFE55P",["bfe55"]),
"b_bfe62a": ("Britânia","BFE62A 62L",62,(34.9,58.3,45.3),None,E,B,"Medida de uma loja só (igual à de outro modelo): confirmar antes de comprar","BFE62A",["bfe62"]),
"b_bfe49pe": ("Britânia","BFE49P 47L de embutir",47,(36,57.5,42.5),None,E,EM,"Ficha oficial do corpo; nicho não informado","BFE49P embutir",["embutir","47"]),
"b_bfr2100": ("Britânia","Air Fryer Oven BFR2100P 12L",12,(32,35,38),None,AF,B,"","BFR2100",["bfr2100"]),
"b_bcfr05": ("Britânia","Bella Cuccina Air Fryer Oven BCFR05 12L",12,(30,31.5,34),None,AF,B,"Ficha oficial; cavidade 18 × 25,4 × 26","BCFR05",["bcfr05"]),
})
S1 += ["b_bfe43","b_bfe44p","b_bfe41p","b_bfe62a"]; U1 += ["b_bfe49","b_bfe55p","b_bfe49pe"]
U2 += ["b_bfr2100","b_bcfr05"]
S3 += ["b_bfe43","b_bfe49","b_bfe55p","b_bfe62a","b_bfe49pe"]
for s in SPACES:
    s["fit"]={"cooktop":S1,"microondas":S2,"airfryer":S3}[s["id"]]; s["over"]={"cooktop":U1,"microondas":U2,"airfryer":U3}[s["id"]]
