#!/usr/bin/env python3
"""Generate the example cards for 'fat-santa', a Christmas deckbuilder with
four resources: Money ($), Reindeer, Sled, Presents.

The three Present (victory) cards follow a 2/5/8 cost -> 1/2/3 presents pattern.

Output is data/fat_santa_cards.csv with columns: name, cost, types, presents,
text. (Cards carry no "set" — the second argument to C() is only a build-time
grouping label used for the summary printed below; it is not written out.)
"""
import csv, collections

cards = []

def C(name, _group, cost, types, text, effects=None, presents=""):
    cards.append({
        "name": name,
        "cost": cost,                     # money cost, e.g. "$4"
        "types": types,
        "presents": presents,             # victory points (presents) at game end
        "effects": effects or {},         # machine-readable resource outputs
        "text": text,
        "_group": _group,                 # build-time grouping only; not written
    })

# ============================ SET: North Pole ============================
# Foundation: basic money / reindeer / sled / present cards + core engine.
S = "North Pole"
C("Spare Change", S, "$0", ["Money"], "+$1", {"Coins": "+1"})
C("Coin Purse", S, "$3", ["Money"], "+$2", {"Coins": "+2"})
C("Gold Hoard", S, "$6", ["Money"], "+$3", {"Coins": "+3"})
C("Peppermint Coin", S, "$4", ["Money"], "+$1\n+1 Buy", {"Coins": "+1", "Buys": "+1"})
C("Yearling Reindeer", S, "$2", ["Reindeer"], "+1 Reindeer", {"Reindeer": "+1"})
C("Sturdy Reindeer", S, "$4", ["Reindeer"], "+2 Reindeer", {"Reindeer": "+2"})
C("Kick Sled", S, "$2", ["Sled"], "+1 Sled", {"Sled": "+1"})
C("Cargo Sled", S, "$5", ["Sled"], "+2 Sled", {"Sled": "+2"})
# The three Present (victory) tiers follow a 2/5/8 cost -> 1/2/3 presents pattern.
C("Stocking Stuffer", S, "$2", ["Present"], "Worth 1 present.", {"Presents": "1"}, "1")
C("Gift Box", S, "$5", ["Present"], "Worth 2 presents.", {"Presents": "2"}, "2")
C("Grand Present", S, "$8", ["Present"], "Worth 3 presents.", {"Presents": "3"}, "3")
C("Lump of Coal", S, "$0", ["Coal"], "Worth -1 present.", {"Presents": "-1"}, "-1")
C("Workshop Elf", S, "$3", ["Action"], "+1 Card\n+2 Actions", {"Cards": "+1", "Actions": "+2"})
C("Toy Stack", S, "$4", ["Action"], "+3 Cards", {"Cards": "+3"})
C("General Store", S, "$5", ["Action"], "+1 Card\n+1 Action\n+1 Buy\n+$1",
  {"Cards": "+1", "Actions": "+1", "Buys": "+1", "Coins": "+1"})
C("Tidy Sack", S, "$2", ["Action"], "+1 Action\nDiscard any number of cards, then draw that many.",
  {"Actions": "+1"})
C("Sorting Table", S, "$5", ["Action"], "+2 Cards\n+1 Action", {"Cards": "+2", "Actions": "+1"})
C("Winter Fair", S, "$5", ["Action"], "+2 Buys\n+$2", {"Buys": "+2", "Coins": "+2"})
C("Extra Hands", S, "$3", ["Action"], "+2 Actions\n+1 Buy", {"Actions": "+2", "Buys": "+1"})
C("Careful Count", S, "$2", ["Action"],
  "+1 Card\n+1 Action\nLook at the top card of your deck. You may discard it.",
  {"Cards": "+1", "Actions": "+1"})
C("Chimney Sweep", S, "$4", ["Action"], "+$2\n+1 Buy", {"Coins": "+2", "Buys": "+1"})
C("Gift Fund", S, "$3", ["Money"], "+$2\nIf you have a Sled in play, +$1.", {"Coins": "+2"})
C("Reindeer Feed", S, "$3", ["Action"], "+2 Reindeer\n+1 Action", {"Reindeer": "+2", "Actions": "+1"})
C("Sled Shed", S, "$4", ["Action"], "+2 Sled\n+1 Action", {"Sled": "+2", "Actions": "+1"})
C("Bell Ringer", S, "$3", ["Action"], "+1 Card\n+1 Action\n+$1", {"Cards": "+1", "Actions": "+1", "Coins": "+1"})
C("North Star", S, "$6", ["Action"], "+3 Cards\n+1 Buy", {"Cards": "+3", "Buys": "+1"})
C("Candy Coins", S, "$4", ["Money"], "+$2\nWhen you play this, +1 Reindeer.", {"Coins": "+2", "Reindeer": "+1"})

# ========================== SET: Santa's Workshop ==========================
# Make, wrap and upgrade presents; convert actions/money into victory points.
S = "Santa's Workshop"
C("Wrapping Station", S, "$4", ["Action"], "+1 Action\nGain a Stocking Stuffer.",
  {"Actions": "+1", "Gain": "Stocking Stuffer"})
C("Toy Maker", S, "$5", ["Action"], "+$2\nGain a Present card costing up to $5.",
  {"Coins": "+2", "Gain": "Present <= $5"})
C("Assembly Line", S, "$6", ["Action"], "+2 Cards\n+1 Action\nYou may play an Action card from your hand.",
  {"Cards": "+2", "Actions": "+1"})
C("Master Craftself", S, "$6", ["Action"],
  "Gain a card costing up to $5 to your hand.\nPut a card from your hand onto your deck.",
  {"Gain": "card <= $5"})
C("Gift Wrap", S, "$3", ["Action"], "+2 Actions\nThe next Present you buy this turn costs $2 less.",
  {"Actions": "+2"})
C("Recycler", S, "$4", ["Action"], "Trash a card from your hand.\nGain a card costing up to $2 more than it.",
  {"Trash": "1"})
C("Present Press", S, "$5", ["Action"],
  "+1 Card\n+1 Action\nYou may trash a Money card from your hand. If you do, gain a Present costing up to $6.",
  {"Cards": "+1", "Actions": "+1"})
C("Cookie Bribe", S, "$3", ["Action"], "+1 Card\n+$2", {"Cards": "+1", "Coins": "+2"})
C("Overtime", S, "$3", ["Action"], "+1 Card\n+2 Actions\nDiscard a card.",
  {"Cards": "+1", "Actions": "+2"})
C("Big Batch", S, "$7", ["Action"], "+2 Cards\nGain 2 Stocking Stuffers.",
  {"Cards": "+2", "Gain": "2x Stocking Stuffer"})
C("Quality Control", S, "$4", ["Action"], "+1 Card\n+1 Action\nYou may trash a card. If you do, +$1.",
  {"Cards": "+1", "Actions": "+1"})
C("Ribbon Roll", S, "$2", ["Money"], "+$1\n+1 Reindeer", {"Coins": "+1", "Reindeer": "+1"})
C("Tinsel Stash", S, "$5", ["Money"], "+$3\n+1 Buy", {"Coins": "+3", "Buys": "+1"})
C("Gingerbread Crew", S, "$5", ["Action"], "+2 Cards\n+2 Actions", {"Cards": "+2", "Actions": "+2"})
C("Inventory", S, "$3", ["Action"],
  "+1 Card\n+1 Action\nLook at the top 2 cards of your deck; put them back in any order.",
  {"Cards": "+1", "Actions": "+1"})
C("Golden Ticket", S, "$5", ["Action"], "+1 Buy\n+$2\nGain a Present costing up to $4.",
  {"Buys": "+1", "Coins": "+2", "Gain": "Present <= $4"})
C("Bulk Order", S, "$6", ["Action"], "+1 Buy\n+$3", {"Buys": "+1", "Coins": "+3"})
C("Craft Fair", S, "$4", ["Action"], "+1 Card\n+1 Action\n+1 Buy", {"Cards": "+1", "Actions": "+1", "Buys": "+1"})
C("Elf Union", S, "$5", ["Action"], "+1 Card\n+2 Actions\n+$1", {"Cards": "+1", "Actions": "+2", "Coins": "+1"})
C("Present Prototype", S, "$0", ["Action"], "+1 Card\n+1 Action", {"Cards": "+1", "Actions": "+1"})
C("Ledger", S, "$3", ["Action"], "+1 Card\n+1 Action\n+1 Buy\nWhen you discard this, +$1.",
  {"Cards": "+1", "Actions": "+1", "Buys": "+1"})
C("Charity Drive", S, "$5", ["Action"], "+$2\nGain a Present costing up to $5; if you do, +1 Card.",
  {"Coins": "+2", "Gain": "Present <= $5"})

# ========================= SET: Sleigh & Stable =========================
# Reindeer, sleds and Delivery cards that convert them into presents.
S = "Sleigh & Stable"
C("Reindeer Stable", S, "$4", ["Action"], "+1 Card\n+1 Action\n+1 Reindeer",
  {"Cards": "+1", "Actions": "+1", "Reindeer": "+1"})
C("Prancing Reindeer", S, "$5", ["Action"], "+2 Reindeer\n+1 Card", {"Reindeer": "+2", "Cards": "+1"})
C("Blitzen Boost", S, "$6", ["Action"], "+3 Reindeer", {"Reindeer": "+3"})
C("Sleigh Bells", S, "$3", ["Action"], "+1 Sled\n+2 Actions", {"Sled": "+1", "Actions": "+2"})
C("Heavy Sled", S, "$6", ["Sled"], "+3 Sled", {"Sled": "+3"})
C("Delivery Run", S, "$5", ["Action", "Delivery"],
  "Delivery: If you have 2+ Reindeer and 1+ Sled this turn, gain a Gift Box.",
  {"Gain": "Gift Box"})
C("Rooftop Drop", S, "$4", ["Action", "Delivery"],
  "Delivery: If you have 2+ Reindeer and 1+ Sled this turn, gain a Stocking Stuffer, then +2 Cards.",
  {"Gain": "Stocking Stuffer", "Cards": "+2"})
C("Express Sleigh", S, "$7", ["Action", "Delivery"],
  "+2 Reindeer\n+2 Sled\nDelivery: gain a Gift Box.", {"Reindeer": "+2", "Sled": "+2", "Gain": "Gift Box"})
C("Midnight Flight", S, "$8", ["Action", "Delivery"],
  "Delivery: If you have 4+ Reindeer and 2+ Sled this turn, gain a Grand Present.",
  {"Gain": "Grand Present"})
C("Team Harness", S, "$4", ["Action"], "+1 Card\n+1 Action\n+1 Reindeer\n+1 Sled",
  {"Cards": "+1", "Actions": "+1", "Reindeer": "+1", "Sled": "+1"})
C("Feed Bag", S, "$2", ["Money"], "+$1\n+1 Reindeer", {"Coins": "+1", "Reindeer": "+1"})
C("Sleigh Garage", S, "$5", ["Action"], "+2 Sled\n+1 Buy", {"Sled": "+2", "Buys": "+1"})
C("Dasher", S, "$5", ["Action"], "+1 Card\n+1 Action\n+2 Reindeer",
  {"Cards": "+1", "Actions": "+1", "Reindeer": "+2"})
C("Dancer", S, "$5", ["Action"], "+2 Reindeer\n+$1", {"Reindeer": "+2", "Coins": "+1"})
C("Vixen", S, "$4", ["Action"], "+1 Card\n+1 Action\n+1 Reindeer",
  {"Cards": "+1", "Actions": "+1", "Reindeer": "+1"})
C("Comet", S, "$6", ["Action"], "+3 Reindeer\n+1 Buy", {"Reindeer": "+3", "Buys": "+1"})
C("Cupid", S, "$4", ["Action"], "+1 Card\n+1 Action\n+1 Sled",
  {"Cards": "+1", "Actions": "+1", "Sled": "+1"})
C("Donner", S, "$5", ["Action"], "+2 Sled\n+1 Card", {"Sled": "+2", "Cards": "+1"})
C("Rudolph", S, "$6", ["Action"],
  "+2 Reindeer\n+2 Sled\nWhile this is in play, your Deliveries need 1 fewer Reindeer.",
  {"Reindeer": "+2", "Sled": "+2"})
C("Loaded Sleigh", S, "$6", ["Action", "Delivery"],
  "Delivery: If you have 3+ Reindeer, gain up to two Gift Boxes (one per 2 Sled you have).",
  {"Gain": "up to 2x Gift Box"})
C("Stable Master", S, "$5", ["Action"], "+1 Card\n+1 Action\n+2 Reindeer",
  {"Cards": "+1", "Actions": "+1", "Reindeer": "+2"})
C("Sled Wright", S, "$4", ["Action"], "+1 Action\nGain a Kick Sled.", {"Actions": "+1", "Gain": "Kick Sled"})
C("Lead Reindeer", S, "$5", ["Reindeer"], "+2 Reindeer\nWhen you play this, +1 Card.",
  {"Reindeer": "+2", "Cards": "+1"})

# ========================= SET: Naughty & Nice =========================
# Attacks, reactions and interactive tricks.
S = "Naughty & Nice"
C("Snowball Fight", S, "$4", ["Action", "Attack"],
  "+$2\nEach other player discards down to 3 cards in hand.", {"Coins": "+2"})
C("Blizzard", S, "$5", ["Action", "Attack"], "+2 Cards\nEach other player gains a Lump of Coal.",
  {"Cards": "+2"})
C("Cozy Blanket", S, "$2", ["Action", "Reaction"],
  "+2 Cards\nWhen another player plays an Attack, you may reveal this from your hand to be unaffected.",
  {"Cards": "+2"})
C("Krampus", S, "$6", ["Action", "Attack"],
  "Each other player discards down to 4 cards in hand and gains a Lump of Coal.")
C("Icy Patch", S, "$5", ["Action", "Attack"],
  "Gain a Reindeer.\nEach other player reveals the top 2 cards of their deck, trashes a revealed Reindeer or Money card, and discards the rest.",
  {"Gain": "Reindeer"})
C("Naughty Prank", S, "$3", ["Action", "Attack"],
  "Each other player with 4+ cards in hand puts one onto their deck.")
C("Warm Cocoa", S, "$3", ["Action", "Reaction"],
  "+1 Card\n+1 Action\nWhen you discard this other than during Clean-up, you may reveal it for +$1.",
  {"Cards": "+1", "Actions": "+1"})
C("Chimney Block", S, "$4", ["Action", "Attack"],
  "+$2\nEach other player with 5+ cards in hand puts one onto their deck.", {"Coins": "+2"})
C("Coal Truck", S, "$5", ["Action", "Attack"],
  "+$2\nEach other player gains a Lump of Coal unless they discard a Present.", {"Coins": "+2"})
C("Elf Spy", S, "$3", ["Action", "Attack"],
  "+1 Card\n+1 Action\nEach player reveals the top card of their deck; you may discard the ones you choose (each other player's, or your own).",
  {"Cards": "+1", "Actions": "+1"})
C("Reindeer Rustler", S, "$5", ["Action", "Attack"],
  "Gain a Sturdy Reindeer.\nEach other player reveals the top 2 cards of their deck, trashes a revealed Reindeer, and discards the rest.",
  {"Gain": "Sturdy Reindeer"})
C("Frostbite", S, "$4", ["Action", "Attack"],
  "Each other player reveals their hand and discards a Sled card if they can.")
C("Nice List Bonus", S, "$5", ["Action"], "+2 Cards\n+1 Buy\nEach other player draws a card.",
  {"Cards": "+2", "Buys": "+1"})
C("Secret Santa", S, "$3", ["Action"],
  "+2 Cards\n+1 Action\nEach player passes a card from their hand to the player on their left, at once.",
  {"Cards": "+2", "Actions": "+1"})
C("Regifting", S, "$4", ["Action"],
  "You may trash a Present from your hand. If you do, +$ equal to its cost plus $1.")
C("Watchdog", S, "$3", ["Action", "Reaction"],
  "+1 Card\n+1 Action\nWhen another player plays an Attack, you may draw a card.",
  {"Cards": "+1", "Actions": "+1"})
C("Snow Fort", S, "$5", ["Action", "Reaction"],
  "+$2\n+1 Buy\nWhen another player plays an Attack, you may reveal this to be unaffected.",
  {"Coins": "+2", "Buys": "+1"})
C("Mischief Elf", S, "$4", ["Action", "Attack"],
  "Each other player discards the top card of their deck. If it is an Action, they gain a Lump of Coal.")
C("Candy Cane Trap", S, "$2", ["Action", "Reaction"],
  "+1 Action\nWhen you would gain a Lump of Coal, you may reveal this from your hand to trash that Coal instead.",
  {"Actions": "+1"})
C("Holiday Cheer", S, "$6", ["Action"], "+2 Cards\n+1 Buy\n+$2", {"Cards": "+2", "Buys": "+1", "Coins": "+2"})
C("Sugar Rush", S, "$3", ["Action"], "+1 Card\n+3 Actions", {"Cards": "+1", "Actions": "+3"})
C("Long Winter", S, "$5", ["Action", "Duration"],
  "Now and at the start of your next turn: +1 Card and +$1.", {"Cards": "+1", "Coins": "+1"})
C("Mrs. Claus", S, "$5", ["Action"],
  "+1 Card\n+1 Action\n+1 Reindeer\n+1 Sled\n+$1",
  {"Cards": "+1", "Actions": "+1", "Reindeer": "+1", "Sled": "+1", "Coins": "+1"})
C("Santa's Sack", S, "$6", ["Action", "Delivery"],
  "Delivery: If you have 3+ Reindeer and 2+ Sled this turn, gain a Present costing up to $8.",
  {"Gain": "Present <= $8"})

# ------------------------------------------------------------------ build
by_group = collections.OrderedDict()
for c in cards:
    by_group.setdefault(c["_group"], 0)
    by_group[c["_group"]] += 1

assert len(cards) == 96, f"expected 96 cards, got {len(cards)}"
names = [c["name"] for c in cards]
dupes = [n for n, k in collections.Counter(names).items() if k > 1]
assert not dupes, f"duplicate names: {dupes}"

# ------------------------------------------------------------------ Rest keyword
# The "Rest" mechanic replaces +Actions on Action cards:
#   +3 Actions -> "The next 2 cards you play this turn lose Rest."
#   +2 Actions -> "The next card you play this turn loses Rest."
#   +1 Action  -> removed (non-terminal; no Rest)
#   no +Action -> gain the keyword "Rest" on a new line at the end
# Non-Action cards (Money/Reindeer/Sled/Present/Coal) are untouched.
import re
REST_1 = "The next card you play this turn loses Rest."
REST_2 = "The next 2 cards you play this turn lose Rest."

def apply_rest(c):
    if "Action" not in c["types"]:
        return
    out, had_plus_action = [], False
    for line in c["text"].split("\n"):
        m = re.fullmatch(r"\+(\d+) Actions?", line.strip())
        if m:
            had_plus_action = True
            n = int(m.group(1))
            if n >= 3:
                out.append(REST_2)
            elif n == 2:
                out.append(REST_1)
            # n == 1: drop the line entirely
            continue
        out.append(line)
    text = "\n".join(out).strip("\n")
    if not had_plus_action:                      # terminal Action card gains Rest
        text = (text + "\n" if text else "") + "Rest"
    c["text"] = text
    c["effects"].pop("Actions", None)

for c in cards:
    apply_rest(c)

# Write a plain CSV (one row per card). No image fields, no "set" column.
# Columns: name, cost, types, presents, text
out = "/home/user/fat-santa/data/fat_santa_cards.csv"
with open(out, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "cost", "types", "presents", "text"])
    for c in cards:
        w.writerow([
            c["name"],
            c["cost"],
            "/".join(c["types"]),
            c["presents"],
            c["text"],                 # newlines within the card text are kept (quoted)
        ])
print("wrote", out)
print("total:", len(cards))
for k, v in by_group.items():
    print(f"  (group) {k}: {v}")
# type distribution
types = collections.Counter()
for c in cards:
    for t in c["types"]:
        types[t] += 1
print("types:", dict(types))
