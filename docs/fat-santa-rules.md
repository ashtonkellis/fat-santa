# fat-santa — game rules (working draft)

**fat-santa** is an original Christmas-themed deckbuilder. This rules doc starts
as a copy of the Dominion rules (`docs/dominion-rules.md`) and is being adapted
to fat-santa one change at a time. **Changes made so far:** the **Rest** keyword
(replaces Dominion's "+Actions"). Everything else below is still the Dominion
baseline and will be updated as the design evolves.

---

## The idea

Every player builds their own deck of cards over the course of the game. You
start with a small, weak deck and use it to buy better cards, which get shuffled
into your deck and improve what you can do on later turns. Cards come in three
broad jobs: **Treasure** (money to spend), **Victory** (points, but dead weight
during play), and **Action** (the engine that does interesting things). Whoever
has the most **victory points** in their deck when the game ends wins.

The tension: Victory cards win the game but do nothing while in your hand, so
buying them clogs your deck. You have to decide when to keep sharpening your
engine and when to start cashing it in for points.

---

## Components & setup

**Each player's starting deck (10 cards):**
- 7 × Copper
- 3 × Estate

Shuffle your 10 cards into a face-down deck and draw a hand of **5**.

**The Supply** (shared, in the middle of the table):

| Pile | Count |
|------|-------|
| Copper | 60 (minus the ones dealt to players) |
| Silver | 40 |
| Gold | 30 |
| Estate | 8 (2 players) / 12 (3–4 players) |
| Duchy | 8 (2 players) / 12 (3–4 players) |
| Province | 8 (2 players) / 12 (3–4 players) |
| Curse | 10 (2p) / 20 (3p) / 30 (4p) |
| Kingdom piles | pick **10** different Kingdom cards, **10 cards each*** |

\* Kingdom piles are 10 cards each, **except** Kingdom cards that are Victory
cards (e.g. Gardens), which use the same count as the other Victory piles: 8 for
2 players, 12 for 3–4.

Decide who goes first (choose randomly).

---

## Card values at a glance

**Treasure (coins when played):**
- Copper = $1 · Silver = $2 · Gold = $3

**Victory (points, counted only at game end):**
- Estate = 1 VP · Duchy = 3 VP · Province = 6 VP
- Curse = **−1 VP**
- Gardens (Kingdom Victory card) = 1 VP for every 10 cards in your deck, rounded down

---

## A turn: A → B → C

Take your whole turn, then play passes to the left. A turn has three phases in
order — **Action, Buy, Clean-up** (easy to remember as **ABC**).

### A — Action phase
Play Action cards from your hand one at a time, resolving each fully before the
next. How long you may keep playing is governed by the **Rest** keyword:

- **Playing a card that has `Rest` ends your turn** — a Rest card is the **last
  card you play this turn**. After it resolves you stop playing cards and move on.
- A card **without** `Rest` does **not** end your turn — after playing it you may
  keep playing more cards.
- **"The next card you play this turn loses Rest."** — the next card you play
  ignores its own `Rest`, so it won't end your turn (your chain continues).
- **"The next 2 cards you play this turn lose Rest."** — the same, applied to your
  next two cards.

Watch for these other keywords while resolving cards:

- **+X Cards** — draw that many cards.
- **+X Buys** — you may buy that many *extra* cards in your Buy phase.
- **+$X** — adds that many coins to spend this turn.

See **[The Rest keyword](#the-rest-keyword)** below for the full explanation and
examples.

### B — Buy phase
1. Play as many **Treasure** cards from your hand as you like, adding up their
   coins (plus any **+$** you earned during your Action phase).
2. Spend those coins to **buy** cards from the Supply. By default you may buy
   **one** card; each **+Buy** you earned lets you buy one more. Your total coins
   are a shared pool you can split across your purchases.
3. A bought card goes to your **discard pile** (not your hand). You may buy a $0
   card even with no coins.

Coins are not tokens — they exist only for this turn. Unspent coins and Buys
vanish at end of turn.

### C — Clean-up phase
- Put everything you played this turn and everything still in your hand into your
  **discard pile**.
- Draw a fresh hand of **5** cards.
- If your deck runs out while drawing, shuffle your discard pile to form a new
  deck and continue.

Then the next player takes their turn.

---

## The Rest keyword

fat-santa replaces Dominion's "+Actions" bookkeeping with a single keyword,
**Rest**.

- **Playing a card that has `Rest` ends your turn.** It is the **last card you
  play this turn**. This is functionally identical to playing a Dominion Action
  that has no "+1 Action" — a *terminal* card.
- A card **without** `Rest` does **not** end your turn. After playing it you may
  keep playing cards. (These are the former "+1 Action" cantrips — the
  "+1 Action" line was simply dropped, because not ending your turn is the
  default for a card with no `Rest`.)
- Two effects let you play *past* a Rest card by stripping the keyword off your
  upcoming cards:
  - **"The next card you play this turn loses Rest."** — your next card ignores
    its own `Rest`, so it no longer ends your turn. (Was **+2 Actions**.)
  - **"The next 2 cards you play this turn lose Rest."** — applies to your next
    two cards. (Was **+3 Actions**.)

In short: `Rest` = terminal (your last card). "Loses Rest" = treat that next card
as non-terminal so your chain can continue.

**Examples**
- **Toy Stack** ($4): "+3 Cards / Rest" — draw 3, then your turn ends.
- **Present Prototype** ($0): "+1 Card" — no `Rest`, so keep playing.
- **Workshop Elf** ($3): "+1 Card / The next card you play this turn loses Rest."
  — draw 1, then your next card won't end your turn even if it has `Rest`.
- **Sugar Rush** ($3): "+1 Card / The next 2 cards you play this turn lose Rest."
  — chain up to two more terminal cards.

---

## Card types you'll meet

Every card has exactly **one** of six types, each shown by its own color (see
`docs/color-scheme.md`):

- **Money** — a simple coin producer (3 tiers: $2/$5/$8 → +$1/+$2/+$3).
- **Reindeer** — produces Reindeer.
- **Sled** — produces Sled.
- **Present** — worth presents at game end (3 tiers: $2/$5/$8 → 1/2/3).
- **Action** — a non-terminal engine card: after playing it you may keep playing.
- **Rest** — a terminal engine card: it's the last card you play this turn (see
  [The Rest keyword](#the-rest-keyword)).

---

## How the game ends & scoring

The game ends immediately at the end of any turn in which **either**:

1. the **Province** pile is empty, **or**
2. **any three** Supply piles are empty (any three, of any kind).

Then everyone shuffles their entire deck together — deck, hand, discard,
everything they own — and totals the victory points on their cards. **Most points
wins.** On a tie, the tied player who has taken the **fewest turns** wins (if
still tied after that, they share the victory).

---

## Quick reference

- **Start:** 7 Copper + 3 Estate; draw 5.
- **Each turn:** play Action cards until you play one with **Rest** → play
  Treasures & buy 1 card → discard all, draw 5.
- **Rest:** a card with `Rest` is the last card you play this turn; "loses Rest"
  lets your next card(s) keep the chain going.
- **Other bonuses:** +Card (draw), +Buy (buy more), +$ (more coins).
- **Money:** Copper $1, Silver $2, Gold $3.
- **Points:** Estate 1, Duchy 3, Province 6, Curse −1.
- **Game ends:** Province pile empty, or any 3 piles empty.
- **Win:** most VP; ties broken by fewest turns taken.

---

_The baseline turn/setup rules here are adapted from the Dominion rules summary
in `docs/dominion-rules.md`; fat-santa's cards and keywords (like Rest) are
original. This is a living draft that changes as the design is specified._
