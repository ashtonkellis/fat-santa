# TODO

## Pending

_Nothing pending._

## Done

- Added shrink-to-fit text to the generator: a "Shrink long text to fit its box" toggle (default on) auto-reduces any overflowing text element's font size so verbose Dominion cards fit their frame's text panel instead of clipping; applies in the editor, deck, print, and PNG export.
- Fine-tuned the frame layout presets: added a third "Corner-number" preset (cost top-left, name top strip, rules across the lower third) and remapped the 12 frames across the simple / templar / corners presets to better match each frame family.
- Wired the Dextrous card frames into the generator: a frame picker (thumbnails of the 12 `assets/card-frames/` frames + None) sets the card's full-bleed background, and choosing a frame auto-applies a matching layout preset (Simple/banner or Templar/gem) that positions the Dominion name/cost/type/text into the frame's regions. Frame art now also prints (background images print-enabled).
- Added a "Print cards" feature to the card list page (`index.html`): prints the currently filtered/searched cards as a print-and-play sheet of real poker-size (63×88 mm) cards, 3 per row on A4.
- Exposed the card list as a GitHub Pages site: added `index.html` (a searchable/filterable/sortable browser of all 538 cards, loaded from `data/dominion_cards.json`, linking to the generator and raw JSON), a `.github/workflows/deploy-pages.yml` Actions workflow, and `.nojekyll`. Requires enabling Pages once in repo Settings (Source: GitHub Actions).
- Downloaded Dextrous's free itch.io asset packs into `assets/`: 12 blank card frames (`assets/card-frames/`, PNG 750×1050) and 6 blank playing-card PDF sheets (`assets/blank-playing-cards/`), with an `assets/README.md` recording source and licensing notes.
- Built `card-generator.html`: a self-contained clone of Dextrous's data-driven card generation feature — design one card layout template (draggable text/image/shape elements bound to data columns via `{{field}}` tokens), point it at CSV/JSON data (one row per card, auto-loads the Dominion dataset), and the whole deck renders live; exports print-ready PDF and per-card PNG. Card sizes: poker/bridge/mini/tarot/square/jumbo/landscape.
- Removed `dominion-randomizer.html` (the kingdom randomizer app).
- Built `dominion-randomizer.html`: a self-contained Dominion kingdom randomizer (expansion picker, generate/reroll/lock, landscape cards, and Colony/Shelters/Potion/Bane rule hints).
- Saved a complete Dominion card list to `data/dominion_cards.json` + `data/dominion_cards.md` (538 cards across 15 sets, sourced from the Dominion Strategy Wiki).
- Set up a TODO list with Pending/Done sections and a CLAUDE.md memory rule to keep it updated.
