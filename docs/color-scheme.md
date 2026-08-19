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
| **Coal** | penalty (−1 present) | dark | `#35353f` |
| _Action / all other cards_ | default card face | subtle Christmas off-white | `#f3f6ef` |

Notes:
- The tint is chosen from a card's **first** type, so e.g. an `Action/Delivery`
  or `Action/Attack` card uses the default Action face.
- Coal is deliberately dark (it's the junk/penalty card), with light text.
- Text, badges, and borders are kept constant across tints for consistency.
