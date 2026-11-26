# Buduje ceny.json dla Skanera Klasera z publicznych plików Cardmarket.
# Uruchamiane automatycznie przez GitHub Actions (plik .github/workflows/strona.yml).
import json, urllib.request, datetime, sys

GRY = {"lorcana": 19, "riftbound": 22, "cyberpunk": 23}
BAZA = "https://downloads.s3.cardmarket.com/productCatalog/"


def pobierz(sciezka):
    req = urllib.request.Request(BAZA + sciezka, headers={"User-Agent": "skaner-klasera"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def cena(v):
    try:
        v = float(v)
    except (TypeError, ValueError):
        return None
    return round(v, 2) if v > 0 else None


wynik = {"at": datetime.date.today().isoformat(), "g": {}}
for gra, gid in GRY.items():
    try:
        produkty = pobierz(f"productList/products_singles_{gid}.json")["products"]
        ceny = {p["idProduct"]: p for p in pobierz(f"priceGuide/price_guide_{gid}.json")["priceGuides"]}
    except Exception as e:  # brak jednej gry nie psuje reszty
        print("Nie pobrano", gra, e, file=sys.stderr)
        continue
    lista = []
    for p in produkty:
        c = ceny.get(p["idProduct"], {})
        lista.append([p["name"], p["idExpansion"], cena(c.get("trend")) or cena(c.get("avg30")),
                      cena(c.get("trend-foil")) or cena(c.get("avg30-foil")), p["idProduct"]])
    wynik["g"][gra] = lista
    print(gra, len(lista), "kart")

with open("ceny.json", "w", encoding="utf-8") as f:
    json.dump(wynik, f, ensure_ascii=False, separators=(",", ":"))
