# fat-santa card color scheme

Cards in the browser (`index.html`) are tinted by their **primary type** so the
resource a card produces is readable at a glance. This file is the canonical
reference for the palette; the same values live as CSS variables in
`index.html` (`:root { --c-money … }`) and as data in
`data/resource_colors.json`.

| Resource / type | Meaning | Color | Hex |
|-----------------|---------|-------|-----|
| **Money** | buy currency | light yellow | `#f7ecc6` |
| **Reindeer** | pulling power | light Christmas green | `#d9edcf` |
| **Sled** | hauling capacity | light blue | `#d4e2f2` |
| **Presents** | victory points | light purple | `#e6dbf4` |
| **Rest** ("stop") | cards with the Rest keyword (terminal — end your turn) | coal grey | `#c3c7cd` |
| _Action / all other cards_ | default card face | subtle Christmas off-white | `#f3f6ef` |

Notes:
- The tint is chosen from a card's **first** type, so e.g. an `Action/Delivery`
  card uses the default Action face.
- **Rest overrides the type tint:** any card whose text carries the standalone
  `Rest` keyword (a terminal card that ends your turn) is coal grey, regardless
  of type. Cards that merely say "…loses Rest" do **not** count.
- Text, badges, and borders are kept constant across tints for consistency.
