# fat-santa card color scheme

Every card has exactly **one** of six types, and each type has its own color.
Cards in the browser (`index.html`) are tinted by that single type. This file is
the canonical reference for the palette; the same values live as CSS variables
in `index.html` (`:root { --c-money … }`) and as data in
`data/resource_colors.json`.

| Type | Meaning | Color | Hex |
|------|---------|-------|-----|
| **Money** | buy currency (3 tiers: $2/$5/$8 → +$1/+$2/+$3) | light yellow | `#f7ecc6` |
| **Reindeer** | pulling power | light Christmas green | `#d9edcf` |
| **Sled** | hauling capacity | light blue | `#d4e2f2` |
| **Present** | victory points (3 tiers: $2/$5/$8 → 1/2/3) | light purple | `#e6dbf4` |
| **Action** | non-terminal engine card | subtle Christmas off-white | `#f3f6ef` |
| **Rest** | terminal engine card (ends your turn) | coal grey | `#c3c7cd` |

Notes:
- **One type per card.** The four resource types (Money/Reindeer/Sled/Present)
  are the simple producer cards. Every other card is either **Action**
  (non-terminal — you may keep playing) or **Rest** (terminal — your last card
  this turn). A card's type is decided in `scripts/gen_fat_santa_cards.py`: a
  former Action card becomes **Rest** if it carries the standalone `Rest`
  keyword, otherwise it stays **Action**.
- Sorting the browser "by type / color" groups cards in the order above.
- Text, badges, and borders are kept constant across tints for consistency.
