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
# The three Money tiers follow a 2/5/8 cost -> +$1/+$2/+$3 pattern.
C("Chimney Change", S, "$2", ["Money"], "+$1", {"Coins": "+1"})
C("Santa's Piggy Bank", S, "$5", ["Money"], "+$2", {"Coins": "+2"})
C("Scrooge's Vault", S, "$8", ["Money"], "+$3", {"Coins": "+3"})
C("Peppermint Coin", S, "$4", ["Action"], "+$1\n+1 Buy", {"Coins": "+1", "Buys": "+1"})
C("Reindeer Energy Drink", S, "$2", ["Reindeer"], "+1 Reindeer", {"Reindeer": "+1"})
C("Magical Reindeer DNA", S, "$5", ["Reindeer"], "+2 Reindeer", {"Reindeer": "+2"})
C("Sleigh Wax Job", S, "$2", ["Sled"], "+1 Sled", {"Sled": "+1"})
C("Turbo Boosters", S, "$5", ["Sled"], "+2 Sled", {"Sled": "+2"})
# The three Present (victory) tiers follow a 2/5/8 cost -> 1/2/3 presents pattern.
C("Toy Conveyor Belt", S, "$2", ["Present"], "Worth 1 present.", {"Presents": "1"}, "1")
C("Robo-Elf Assistant", S, "$5", ["Present"], "Worth 2 presents.", {"Presents": "2"}, "2")
C("Fully Automated Toy Factory", S, "$8", ["Present"], "Worth 3 presents.", {"Presents": "3"}, "3")
C("Workshop Elf", S, "$3", ["Action"], "+1 Card\n+2 Actions", {"Cards": "+1", "Actions": "+2"})
C("Mountain of Toys", S, "$4", ["Action"], "+3 Cards", {"Cards": "+3"})
C("Elf-Mart", S, "$5", ["Action"], "+1 Card\n+1 Action\n+1 Buy\n+$1",
  {"Cards": "+1", "Actions": "+1", "Buys": "+1", "Coins": "+1"})
C("Spring Cleaning", S, "$2", ["Action"], "+1 Action\nDiscard any number of cards, then draw that many.",
  {"Actions": "+1"})
C("Letter-Sorting Frenzy", S, "$5", ["Action"], "+2 Cards\n+1 Action", {"Cards": "+2", "Actions": "+1"})
C("Winter Fair", S, "$5", ["Action"], "+2 Buys\n+$2", {"Buys": "+2", "Coins": "+2"})
C("All Hands on Deck", S, "$3", ["Action"], "+2 Actions\n+1 Buy", {"Actions": "+2", "Buys": "+1"})
C("Checking It Twice", S, "$2", ["Action"],
  "+1 Card\n+1 Action\nLook at the top card of your deck. You may discard it.",
  {"Cards": "+1", "Actions": "+1"})
C("Chimney Sweep", S, "$4", ["Action"], "+$2\n+1 Buy", {"Coins": "+2", "Buys": "+1"})
C("Care Package", S, "$3", ["Action"], "+1 Reindeer\n+1 Sled\n+$1",
  {"Reindeer": "+1", "Sled": "+1", "Coins": "+1"})
C("Reindeer Feed", S, "$3", ["Action"], "+2 Reindeer\n+1 Action", {"Reindeer": "+2", "Actions": "+1"})
C("Sled Shed", S, "$4", ["Action"], "+2 Sled\n+1 Action", {"Sled": "+2", "Actions": "+1"})
C("Bell Ringer", S, "$3", ["Action"], "+1 Card\n+1 Action\n+$1", {"Cards": "+1", "Actions": "+1", "Coins": "+1"})
C("North Star", S, "$6", ["Action"], "+3 Cards\n+1 Buy", {"Cards": "+3", "Buys": "+1"})
C("Candy Coins", S, "$4", ["Action"], "+$2\n+1 Reindeer", {"Coins": "+2", "Reindeer": "+1"})

# ========================== SET: Santa's Workshop ==========================
# Make, wrap and upgrade presents; convert actions/money into victory points.
S = "Santa's Workshop"
C("Gift-Wrapping Frenzy", S, "$4", ["Action"], "+1 Action\nGain a Toy Conveyor Belt.",
  {"Actions": "+1", "Gain": "Toy Conveyor Belt"})
C("Toy Maker", S, "$5", ["Action"], "+$2\nGain a Present card costing up to $5.",
  {"Coins": "+2", "Gain": "Present <= $5"})
C("Toy Assembly Line", S, "$6", ["Action"], "+2 Cards\n+1 Action\nYou may play an Action card from your hand.",
  {"Cards": "+2", "Actions": "+1"})
C("Master Craftself", S, "$6", ["Action"],
  "Gain a card costing up to $5 to your hand.\nPut a card from your hand onto your deck.",
  {"Gain": "card <= $5"})
C("Gift Wrap", S, "$3", ["Action"], "+2 Actions\nThe next Present you buy this turn costs $2 less.",
  {"Actions": "+2"})
C("Toy Recycler", S, "$4", ["Action"], "Trash a card from your hand.\nGain a card costing up to $2 more than it.",
  {"Trash": "1"})
C("Gift Compactor", S, "$5", ["Action"],
  "+1 Card\n+1 Action\nYou may trash a Money card from your hand. If you do, gain a Present costing up to $6.",
  {"Cards": "+1", "Actions": "+1"})
C("Cookie Bribe", S, "$3", ["Action"], "+1 Card\n+$2", {"Cards": "+1", "Coins": "+2"})
C("Elf Overtime", S, "$3", ["Action"], "+1 Card\n+2 Actions\nDiscard a card.",
  {"Cards": "+1", "Actions": "+2"})
C("Mass Toy Production", S, "$7", ["Action"], "+2 Cards\nGain 2 Toy Conveyor Belts.",
  {"Cards": "+2", "Gain": "2x Toy Conveyor Belt"})
C("Quality Elf-spection", S, "$4", ["Action"], "+1 Card\n+1 Action\nYou may trash a card. If you do, +$1.",
  {"Cards": "+1", "Actions": "+1"})
C("Ribbon Roll", S, "$2", ["Action"], "+$1\n+1 Reindeer", {"Coins": "+1", "Reindeer": "+1"})
C("Tinsel Stash", S, "$5", ["Action"], "+$3\n+1 Buy", {"Coins": "+3", "Buys": "+1"})
C("Gingerbread Crew", S, "$5", ["Action"], "+2 Cards\n+2 Actions", {"Cards": "+2", "Actions": "+2"})
C("Naughty-or-Nice Audit", S, "$3", ["Action"],
  "+1 Card\n+1 Action\nLook at the top 2 cards of your deck; put them back in any order.",
  {"Cards": "+1", "Actions": "+1"})
C("Golden Ticket", S, "$5", ["Action"], "+1 Buy\n+$2\nGain a Present costing up to $4.",
  {"Buys": "+1", "Coins": "+2", "Gain": "Present <= $4"})
C("Wholesale Toys", S, "$6", ["Action"], "+1 Buy\n+$3", {"Buys": "+1", "Coins": "+3"})
C("Craft Fair", S, "$4", ["Action"], "+1 Card\n+1 Action\n+1 Buy", {"Cards": "+1", "Actions": "+1", "Buys": "+1"})
C("Elf Union", S, "$5", ["Action"], "+1 Card\n+2 Actions\n+$1", {"Cards": "+1", "Actions": "+2", "Coins": "+1"})
C("Present Prototype", S, "$0", ["Action"], "+1 Card\n+1 Action", {"Cards": "+1", "Actions": "+1"})
C("Santa's Ledger", S, "$3", ["Action"], "+1 Card\n+1 Action\n+1 Buy\nWhen you discard this, +$1.",
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
C("Rocket Sleigh Engine", S, "$8", ["Sled"], "+3 Sled", {"Sled": "+3"})
C("Delivery Run", S, "$5", ["Action"],
  "Spend 2 Reindeer and 1 Sled: gain a Robo-Elf Assistant.",
  {"Gain": "Robo-Elf Assistant"})
C("Rooftop Drop", S, "$4", ["Action"],
  "Spend 1 Reindeer and 1 Sled: gain a Toy Conveyor Belt.\n+1 Card",
  {"Gain": "Toy Conveyor Belt", "Cards": "+1"})
C("Express Sleigh", S, "$7", ["Action"],
  "+3 Reindeer\n+2 Sled\n+1 Card", {"Reindeer": "+3", "Sled": "+2", "Cards": "+1"})
C("Midnight Flight", S, "$8", ["Action"],
  "Spend 4 Reindeer and 2 Sled: gain a Fully Automated Toy Factory.\n+2 Cards",
  {"Gain": "Fully Automated Toy Factory", "Cards": "+2"})
C("Team Harness", S, "$4", ["Action"], "+1 Card\n+1 Action\n+1 Reindeer\n+1 Sled",
  {"Cards": "+1", "Actions": "+1", "Reindeer": "+1", "Sled": "+1"})
C("Feed Bag", S, "$2", ["Action"], "+$1\n+1 Reindeer", {"Coins": "+1", "Reindeer": "+1"})
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
  "+2 Reindeer\n+2 Sled\nWhile this is in play, your Spend costs need 1 fewer Reindeer.",
  {"Reindeer": "+2", "Sled": "+2"})
C("Loaded Sleigh", S, "$6", ["Action"],
  "Spend 2 Reindeer and 2 Sled: gain a Robo-Elf Assistant.\n+$2",
  {"Gain": "Robo-Elf Assistant", "Coins": "+2"})
C("Stable Master", S, "$5", ["Action"], "+1 Card\n+1 Action\n+2 Reindeer",
  {"Cards": "+1", "Actions": "+1", "Reindeer": "+2"})
C("Sleigh Mechanic", S, "$4", ["Action"], "+1 Action\nGain a Sleigh Wax Job.", {"Actions": "+1", "Gain": "Sleigh Wax Job"})
C("Bionic Antler Upgrade", S, "$8", ["Reindeer"], "+3 Reindeer", {"Reindeer": "+3"})

# ========================= SET: Naughty & Nice =========================
# Interactive tricks and effects (no attacks, no reactions).
S = "Naughty & Nice"
C("Nice List Bonus", S, "$5", ["Action"], "+2 Cards\n+1 Buy\nEach other player draws a card.",
  {"Cards": "+2", "Buys": "+1"})
C("Secret Santa", S, "$3", ["Action"],
  "+2 Cards\n+1 Action\nEach player passes a card from their hand to the player on their left, at once.",
  {"Cards": "+2", "Actions": "+1"})
C("Regifting", S, "$4", ["Action"],
  "You may trash a Present from your hand. If you do, +$ equal to its cost plus $1.")
C("Holiday Cheer", S, "$6", ["Action"], "+2 Cards\n+1 Buy\n+$2", {"Cards": "+2", "Buys": "+1", "Coins": "+2"})
C("Sugar Rush", S, "$3", ["Action"], "+1 Card\n+3 Actions", {"Cards": "+1", "Actions": "+3"})
C("Long Winter", S, "$5", ["Action"],
  "Now and at the start of your next turn: +1 Card and +$1.", {"Cards": "+1", "Coins": "+1"})
C("Mrs. Claus", S, "$5", ["Action"],
  "+1 Card\n+1 Action\n+1 Reindeer\n+1 Sled\n+$1",
  {"Cards": "+1", "Actions": "+1", "Reindeer": "+1", "Sled": "+1", "Coins": "+1"})
C("Santa's Sack", S, "$6", ["Action"],
  "Spend 3 Reindeer and 2 Sled: gain a Present costing up to $8.",
  {"Gain": "Present <= $8"})

# ------------------------------------------------------------------ build
by_group = collections.OrderedDict()
for c in cards:
    by_group.setdefault(c["_group"], 0)
    by_group[c["_group"]] += 1

assert len(cards) == 79, f"expected 79 cards, got {len(cards)}"
names = [c["name"] for c in cards]
dupes = [n for n, k in collections.Counter(names).items() if k > 1]
assert not dupes, f"duplicate names: {dupes}"

# ------------------------------------------------------------------ Rest keyword
# The "Rest" mechanic replaces +Actions on Action cards:
#   +3 Actions -> "The next 2 cards you play this turn lose Rest."
#   +2 Actions -> "The next card you play this turn loses Rest."
#   +1 Action  -> removed (non-terminal; no Rest)
#   no +Action -> gain the keyword "Rest" on a new line at the end
# Non-Action cards (Money/Reindeer/Sled/Present) are untouched.
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

# ------------------------------------------------------------------ single type
# Every card ends up with exactly ONE of the six types:
#   Money / Reindeer / Sled / Present  (resource producers)
#   Action  (non-terminal engine card)
#   Rest    (terminal engine card — ends your turn)
# Resource cards keep their type; former Action cards become Rest if terminal
# (they carry the standalone "Rest" keyword) else stay Action. Any secondary
# types (Delivery/Duration) were already dropped at definition.
def has_rest_keyword(c):
    return any(line.strip() == "Rest" for line in c["text"].split("\n"))

for c in cards:
    if c["types"] == ["Action"]:
        c["types"] = ["Rest"] if has_rest_keyword(c) else ["Action"]

SIX = {"Money", "Reindeer", "Sled", "Present", "Action", "Rest"}
for c in cards:
    assert len(c["types"]) == 1 and c["types"][0] in SIX, \
        f"{c['name']} has bad type {c['types']}"

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
