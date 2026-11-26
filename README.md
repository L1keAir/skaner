# Skaner Klasera

Skaner kart TCG (Lorcana, Riftbound, Cyberpunk) z kamerą na żywo. Zeskanowane karty trafiają do Klasera przez plik: w skanerze „Wyślij do Klasera”, w Klaserze zakładka Skaner → „Importuj ze Skanera”.

- `index.html` – aplikacja skanera
- `ceny.py` – co dzień buduje `ceny.json` z publicznych cenników Cardmarket
- `.github/workflows/strona.yml` – publikuje stronę na GitHub Pages i odświeża ceny codziennie rano
- `manifest.webmanifest`, `icon-*.png` – instalacja na ekranie głównym telefonu

Klucz API Anthropic (opcjonalny) wpisuje się w ustawieniach skanera. Zostaje tylko w pamięci telefonu i nigdy nie trafia do tego repozytorium.
