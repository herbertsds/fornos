# Projeto: fornos para a cozinha do Herbert

Este documento passa o trabalho feito numa conversa com o Claude (app) para o Claude Code continuar. Responda sempre em português.

## 1. Objetivo

O Herbert está escolhendo um forno para a cozinha de casa. Mediu três espaços possíveis. A meta é encontrar os **maiores** fornos (elétricos ou a gás, de bancada ou de embutir, vendidos no Brasil) que cabem em cada espaço, e também os que passam um pouco. Ele quer comparar tudo num site pensado **primeiro para o celular**.

### Os três espaços (medidas da foto que ele mandou)

| id | Espaço | Largura | Altura | Profundidade |
|---|---|---|---|---|
| cooktop | Sob o cooktop | 62 | 35 | 50 |
| microondas | Sobre o micro-ondas | 57 | 43,5 | 29 |
| airfryer | Antigo lugar da air fryer | 67 | 71 | 48,5 |

No código as medidas ficam na ordem **A × L × P** (altura, largura, profundidade), em cm.

### Conclusões que já valem

- **Sobre o micro-ondas** a profundidade de 29 cm só aceita mini fornos de 6 a 10 L.
- **A gás:** nenhum forno doméstico cabe. Os de embutir têm uns 58 a 61 cm de profundidade, e o nicho exigido também não cabe. As opções a gás aparecem como "Ultrapassa".
- **Consul e Brastemp:** só vendem fornos de embutir, de uns 58 cm de profundidade. Nenhum cabe.
- **Embutir:** o encaixe usa a **medida do nicho exigido pelo fabricante** (campo `nc`) quando ela existe, não só o corpo. Midea TSD62, Electrolux OE60M, Samsung, Dako, Continental, Fischer Infinity e Brastemp BOA84 têm `nc`.
- **Ventilação:** os manuais pedem uns 10 a 15 cm de folga em volta dos fornos de bancada. O site compara só o corpo do forno com o espaço.

## 2. Linha do tempo dos pedidos

1. Busca extensa (Consul, Brastemp, Electrolux, Oster, Midea e outras): pelo menos 10 que cabem e uns 10 que passam um pouco, por espaço.
2. Medidas internas em todas as linhas.
3. Até 3 links de compra por linha.
4. Toda a linha da Mondial, mais colunas de Amazon e Mercado Livre.
5. Separar por tipo (gás, elétrico, outros). Pelo menos 5 fotos por modelo. Site hospedado com filtro de tipo, comparação visual (espaço × forno × interno, em texto e desenho), ordenação por valor, capacidade e maior encaixe.
6. Menor e maior valor com o nome da loja; espaço fixo para Mercado Livre e Amazon; seção recolhível com todos os links.
7. Responsivo, com o celular como prioridade.
8. **Pendente:** 5 vídeos de review no YouTube por modelo, do mais visto ao menos visto, e reviews escritos com texto suficiente para uma análise de verdade.
9. **Pendente:** procurar fornos no Hardmob Promoções, Gatry e Promobit. Se for um modelo da lista, ler os comentários. Se for novo, ver se cabe e incluir.
10. Filtros de bancada/embutir, litragem mínima e medida interna mínima.
11. Favoritos marcados por espaço, vistos por espaço ou todos juntos, salvos no localStorage. Os filtros também valem para os favoritos.
12. Carrossel de fotos em loop.
13. Cinco marcas novas: Tramontina, Dako, Continental, Cadence e Layr. Depois Philips, Philco (já existia), Samsung e LG. Filtro de marca com várias escolhas.
14. Modo claro como padrão.
15. Busca extensa da Britânia.
16. Filtros quebram de linha (sem rolagem lateral), filtro "Todos / Só os que cabem" visível, ordenação padrão por litragem, links e preços **reais** do Mercado Livre e da Amazon nos cards (**parcial**, ver seção 6).
17. Subir o site no servidor dele na Oracle (é a sua tarefa) e usar **todas as fotos disponíveis, sem limite**.

## 3. O que existe hoje

- **Site publicado como artefato do Claude:** https://claude.ai/artifact/Tr8GZTKhV9Ux9Hury74sko. Só fica visível para a conta dele.
  - O artefato aceita no máximo 512 arquivos, por isso lá as fotos estão limitadas a 6 por modelo.
  - No servidor próprio não existe esse limite. Gere com todas as fotos (seção 5).
- **Planilha (Claude Sheets):** https://claude.ai/artifact/BGMz4KYVh7nKiTr9tqpicZ. É a versão antiga, de antes do site, com as abas por espaço e os links. Não precisa mexer.
- **92 modelos** ao todo, de 26 marcas:
  - Arno, Best, Black+Decker, Brastemp, Britânia, Consul, Continental, Dako, Electrolux, Elgin, Fischer, Fogatti, Midea, Mondial, Mueller
  - Nardelli, Oster, Philco, Philips Walita, Samsung, Suggar, Terim, Tramontina, Venax
- **Ficaram de fora por falta de medidas confiáveis:**
  - Cadence: FOR310, FOR451, FOR455, FOR560, FOR650
  - Layr
  - Mondial: FR-17, FR-08, FR-13
  - Britânia: BFE36P, BFE45PI, BFE25P, BFE47P
- **LG:** no Brasil só tem um forno de embutir de 133 L, grande demais para os três espaços.
- **Sem nenhuma foto nas lojas consultadas (11 modelos):**
  - Philco: PFE50PE
  - Oster: OFOR310, Compact 10L
  - Mondial: FR-20
  - Arno: FOR1
  - Elgin: FOR090
  - Suggar: FE09
  - Black+Decker: TO1745, TO3250
  - Electrolux: FB54X
  - Venax: industrial 77L

## 4. Arquivos deste pacote

```
site/                  site pronto para subir (index.html + i/*.webp), igual ao artefato publicado
fonte/
  data.py              modelos (medidas, tipo, instalação, observação, termo de busca) e quais entram em cada espaço
  fetch.py             busca ofertas e fotos nas APIs públicas de catálogo VTEX das lojas e grava vtex.json
  build.py             baixa as fotos, tira as quase-duplicadas, junta tudo e gera dist/ (index.html + i/ + site.json)
  template.html        o site (HTML/CSS/JS num arquivo só); build.py troca __DATA__ pelos dados
  vtex.json            última coleta (12/11/2026): ofertas por loja, preços e URLs de fotos (sem limite, até 60 por modelo)
  extras.json          dados manuais: preços e links de Mercado Livre/Amazon (campo x) e nichos de embutir (campo nc)
  site.json            dados do site publicado hoje (referência)
  specs.py, newbrands.py   scripts auxiliares que exploraram as especificações das lojas
CONTEXTO.md            este arquivo
```

### Estrutura de `data.M[chave]`

```
(marca, modelo, litros, (A, L, P), (A_int, L_int, P_int) ou None,
 tipo: "Elétrico" | "Elétrico + air fryer" | "Gás",
 instalação: "Bancada" | "Embutir",
 observação, termo de busca, palavras obrigatórias no nome do produto)
```

Em `OV`, no `fetch.py`, há termos de busca, regex obrigatórias e regex proibidas por modelo. Eles existem para evitar produto errado, como acessórios ou outro modelo da mesma família.

`data.SPACES` diz, para cada espaço, quais chaves aparecem como "cabe" (`fit`) e como "ultrapassa" (`over`). No site, o status final é recalculado pelas medidas: usa `nc` se existir, senão `d`.

### Estrutura de `site.json`, usada pelo template

`models[k]` tem os campos:

- `b`: marca
- `m`: modelo
- `l`: litros
- `d`: [A, L, P]
- `i`: medidas internas [A, L, P] ou null
- `t`: tipo
- `mt`: instalação
- `n`: observação
- `img`: números dos arquivos `i/N.webp`
- `o`: ofertas, cada uma `[loja, nome, preço ou null, link]`
- `q`: termo de busca usado nos links de Amazon e Mercado Livre
- `x`: `{ml: {u, p, d}, amz: {u, p, d}}`, com link do anúncio real, preço e data em que foi visto
- `nc`: nicho [A, L, P], opcional

`spaces`: `[{id, name, d: [A, L, P], fit: [...], over: [...]}]`

## 5. Como gerar e subir com todas as fotos

```bash
cd fonte
pip install pillow            # se faltar
python3 fetch.py              # opcional: atualiza preços e fotos das lojas (uns 5 a 8 min)
python3 build.py              # todas as fotos, sem limite; gera fonte/dist/
# depois sirva fonte/dist/ como site estático
```

- `build.py --max-fotos 6` gera a versão limitada, igual à do artefato.
- São cerca de 3.300 URLs de foto antes de tirar as duplicadas. Muitas se repetem entre lojas e voltagens.
- O site é estático: só `index.html` e `i/`. As fontes vêm do Google Fonts. Não há backend.
- O estado de cada pessoa fica no localStorage do navegador:
  - `fornos2`: filtros
  - `fornosFav`: favoritos, no formato `"<espaço>:<chave>"`

**Deploy sugerido:** container `httpd:2.4` ou `nginx:alpine` servindo a pasta (somente leitura), na rede Docker do Nginx Proxy Manager, sem porta pública, com Proxy Host e SSL do Let's Encrypt.

- Pergunte ao Herbert qual domínio usar antes de criar a rota.
- Não mexa nos outros projetos do servidor (Alumni UFRJ, Mapa da Empregabilidade, Orienta.AI).

## 6. Fontes de dados e limitações

- **Preços e fotos:** vêm das APIs públicas de catálogo VTEX (`/api/catalog_system/pub/products/search?ft=...`):
  - lojas oficiais: Mondial, Philco, Britânia, Electrolux, Brastemp, Consul, Oster, Midea, Elgin, Arno, Dako, Continental
  - varejo: Fast Shop, Webcontinental, Lojas MM
  - o menor e o maior valor mostrados no card saem dessas ofertas
- **Casas Bahia, Extra e Ponto Frio** bloqueiam acesso automatizado (403). As medidas dessas lojas vieram de trechos de busca na web.
- **Mercado Livre e Amazon** bloqueiam leitura direta (robots).
  - Até agora só existem links reais de anúncio e preço para 10 modelos na Amazon e 1 no Mercado Livre (ver `extras.json`). Mais 2 modelos têm só o preço, sem link: PFE51P na Amazon e FRN-48-BI no Mercado Livre.
  - O resto mostra "Ver preços", que abre a busca do site.
  - Não contorne bloqueio de robôs nem verificação anti-bot.
- **Medidas:** quando as fontes divergem, o valor usado e a outra versão ficam no campo `n`.
  - As fichas técnicas oficiais da Britânia/Philco (`suporte.britania.com.br`, medidas em mm na linha "Produto") foram priorizadas.

## 7. Próximos passos pendentes, na ordem que fizer sentido para o Herbert

1. **Subir o site no servidor da Oracle**, com todas as fotos.
2. **Links e preços reais** do Mercado Livre e da Amazon para os modelos que faltam, sem contornar bloqueios.
3. **YouTube:** pelo menos 5 vídeos de review por modelo, do mais visto ao menos visto. Se não der para ler o número de visualizações, deixe isso claro. Mostrar no card numa seção recolhível.
4. **Reviews escritos** com conteúdo de verdade, não só ficha técnica, por modelo.
5. **Hardmob Promoções, Gatry e Promobit:**
   - modelo da lista: resumir os comentários das promoções;
   - modelo novo: checar se cabe em algum espaço e incluir em `data.py`.
6. **Medidas que faltam:** completar Cadence, Layr, Mondial FR-17 e os Britânia citados, e fotos dos 11 modelos sem foto.

Antes de cada etapa grande, confirme com o Herbert. Ele prefere avançar passo a passo, confirmando cada fase.
