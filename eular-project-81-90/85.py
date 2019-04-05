import random

random.seed(0)

########


squares = [
  "GO",  "A1", "CC1",  "A2",  "T1",  "R1",  "B1", "CH1",  "B2",  "B3",
"JAIL",  "C1",  "U1",  "C2",  "C3",  "R2",  "D1", "CC2",  "D2",  "D3",
  "FP",  "E1", "CH2",  "E2",  "E3",  "R3",  "F1",  "F2",  "U2",  "F3",
 "G2J",  "G1",  "G2", "CC3",  "G3",  "R4", "CH3",  "H1",  "T2",  "H2"
]


NUM_SQUARES = len(squares)
NUM_DIE_SIDES = 4
DEBUG = False


########


def die():
  return random.randrange(1, NUM_DIE_SIDES + 1)

def dice():
  return die(), die()


########


def s_to_i(square):
  return squares.index(square)

def i_to_s(i):
  return squares[i]


########

def ident(current_square):
  return current_square

def nextR(current_square):
  i = s_to_i(current_square)
  while squares[i][0] != "R":
    i = (i + 1) % NUM_SQUARES
  return i_to_s(i)

def nextU(current_square):
  i = s_to_i(current_square)
  while squares[i][0] != "U":
    i = (i + 1) % NUM_SQUARES
  return i_to_s(i)

def back3(current_square):
  i = s_to_i(current_square)
  # Python actually has sensible sign semantics for modulus,
  # but enough languages have made the wrong choice, so I'm always paranoid.
  return i_to_s((i + NUM_SQUARES - 3) % NUM_SQUARES)

CC_cards = [
  ident, ident, ident, ident,
  ident, ident, ident, ident,
  ident, ident, ident, ident,
  ident, ident,
  "GO",
  "JAIL"
]

CH_cards = [
  ident, ident, ident, ident,
  ident, ident,
  "GO",
  "JAIL",
  "C1",
  "E3",
  "H2",
  "R1",
  nextR,
  nextR,
  nextU,
  back3
]

########


def simulation(num_games, num_turns, turns_to_burn):

  frequencies = {}
  for square in squares:
    frequencies[square] = 0

  for sim in range(num_games):

    current_square = "GO"

    # Copying lists: it's so obvious!
    decks = {
     "CC": list(CC_cards),
     "CH": list(CH_cards)
    }

    # Let's shuffle! In place? Why not‽ We have no other choice!
    random.shuffle(decks["CC"])
    random.shuffle(decks["CH"])

    for turn in range(num_turns + turns_to_burn):
      if DEBUG: print("[Sim %d][Turn %d] Currently on: %s (Square %d)" % (sim, turn, current_square, s_to_i(current_square)))

      continueRolling = True
      numDoubles = 0
      while continueRolling:

        if (turn >= turns_to_burn):
          frequencies[current_square] += 1

        d1, d2 = dice()
        continueRolling = (d1 == d2)

        if DEBUG: print("[Sim %d][Turn %d] Rolled [%d, %d] => %d (Doubles? %r)" % (sim, turn, d1, d2, d1+d2, continueRolling))

        if (continueRolling):
          numDoubles += 1
          if (numDoubles == 3):
            if DEBUG: print("[Sim %d][Turn %d] Rolled three doubles. Going to JAIL." % (sim, turn))
            current_square = "JAIL"
            continue

        i = squares.index(current_square)
        i = (i + d1 + d2) % NUM_SQUARES
        current_square = i_to_s(i)

        CC_or_CH = current_square[:2]

        if current_square == "G2J":
          current_square = "JAIL"
          # In real Monopoly, the turn ends.
          # The problem description is not clear about this. :-/
          continue
        elif CC_or_CH in ["CC", "CH"]:

          card = decks[CC_or_CH][0]
          decks[CC_or_CH] = decks[CC_or_CH][1:] + [card]

          if isinstance(card, str):
            current_square = card
          elif callable(card): 
            current_square = card(current_square)
          else:
            assert False # Trust no one.

          # HEY, PROBLEM STATEMENT. GET YOUR ACT TOGETHER.
          if current_square == "JAIL":
            continue

  return frequencies


frequencies = simulation(num_games=1, num_turns=100000, turns_to_burn=100)
sorted_frequencies = sorted(frequencies, key=frequencies.get)

if DEBUG: print(sorted(frequencies.items(), key=lambda x:x[1]))

result = ""
# Convert to a list because APPARENTLY PYTHON CAN'T SLICE THE FRONT OF A GENERATOR WITHOUT IMPORTING ITERTOOLS.
for square in list(reversed(sorted_frequencies))[:3]:
  result += "%02d" % s_to_i(square)

print(result)
