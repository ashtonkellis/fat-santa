# fat-santa card color scheme

Every card has exactly **one** of six types, and each type has its own color.
Cards in the browser (`index.html`) are tinted by that single type. This file is
the canonical reference for the palette; the same values live as CSS variables
in `index.html` (`:root { --c-money … }`) and as data in
`data/resource_colors.json`.

On the full-art cards the type color shows as the **thick card border** (and,
for the four resources, the **colored ring** around the rail icon). The `Border`
column is that identity color; the `Fallback bg` is a pale tint shown only if a
card's art fails to load.

| Type | Meaning | Border | Border hex | Fallback bg |
|------|---------|--------|-----------|-------------|
| **Money** | buy currency (3 tiers: $1/$4/$7 → +$1/+$2/+$3) | gold | `#c9962a` | `#f7ecc6` |
| **Reindeer** | pulling power | Christmas green | `#3f8f43` | `#d9edcf` |
| **Sled** | hauling capacity | blue | `#2f6fb0` | `#d4e2f2` |
| **Present** | victory points (3 tiers: $1/$4/$7 → 1/2/3) | purple | `#7a4fb0` | `#e6dbf4` |
| **Action** | non-terminal engine card | grey | `#6b7078` | `#f3f6ef` |
| **Rest** | terminal engine card ("stop" — ends your turn) | Christmas red | `#c1272d` | `#c3c7cd` |

Notes:
- **One type per card.** The four resource types (Money/Reindeer/Sled/Present)
  are the simple producer cards. Every other card is either **Action**
  (non-terminal — you may keep playing) or **Rest** (terminal — your last card
  this turn). A card's type is decided in `scripts/gen_fat_santa_cards.py`: a
  former Action card becomes **Rest** if it carries the standalone `Rest`
  keyword, otherwise it stays **Action**.
- Sorting the browser "by type / color" groups cards in the order above.
- Text, badges, and borders are kept constant across tints for consistency.
