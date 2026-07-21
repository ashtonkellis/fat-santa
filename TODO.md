# TODO

## Pending

_Nothing pending._

## Done

- Exposed the card list as a GitHub Pages site: added `index.html` (a searchable/filterable/sortable browser of all 538 cards, loaded from `data/dominion_cards.json`, linking to the generator and raw JSON), a `.github/workflows/deploy-pages.yml` Actions workflow, and `.nojekyll`. Requires enabling Pages once in repo Settings (Source: GitHub Actions).
- Downloaded Dextrous's free itch.io asset packs into `assets/`: 12 blank card frames (`assets/card-frames/`, PNG 750×1050) and 6 blank playing-card PDF sheets (`assets/blank-playing-cards/`), with an `assets/README.md` recording source and licensing notes.
- Built `card-generator.html`: a self-contained clone of Dextrous's data-driven card generation feature — design one card layout template (draggable text/image/shape elements bound to data columns via `{{field}}` tokens), point it at CSV/JSON data (one row per card, auto-loads the Dominion dataset), and the whole deck renders live; exports print-ready PDF and per-card PNG. Card sizes: poker/bridge/mini/tarot/square/jumbo/landscape.
- Removed `dominion-randomizer.html` (the kingdom randomizer app).
- Built `dominion-randomizer.html`: a self-contained Dominion kingdom randomizer (expansion picker, generate/reroll/lock, landscape cards, and Colony/Shelters/Potion/Bane rule hints).
- Saved a complete Dominion card list to `data/dominion_cards.json` + `data/dominion_cards.md` (538 cards across 15 sets, sourced from the Dominion Strategy Wiki).
- Set up a TODO list with Pending/Done sections and a CLAUDE.md memory rule to keep it updated.
