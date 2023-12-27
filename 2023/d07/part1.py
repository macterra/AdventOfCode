# https://adventofcode.com/2023/day/7

import functools

input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

def rank(card):
    ranks = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10
    }

    return int(card) if card.isdigit() else ranks[card]

def compareHands(a, b):
    ra, rb = a["rank"], b["rank"]
    ca, cb = a["cards"], b["cards"]

    if ra != rb:
        return -1 if ra < rb else 1
    else:
        return -1 if ca < cb else 1

def parse(input):
    hands = []
    for line in input.split('\n')[:-1]:
        hand = {}
        cards, bid = line.split(' ')
        cards = [rank(card) for card in cards]
        for card in cards:
            if not card in hand:
                hand[card] = 1
            else:
                hand[card] += 1
        hand["rank"] = sorted(hand.values())[::-1]
        hand["cards"] = cards #sorted(cards)[::-1]
        hand["bid"] = int(bid)
        hands.append(hand)
    return hands


input = open('data', 'r').read()

hands = parse(input)
hands = sorted(hands, key=functools.cmp_to_key(compareHands))

sum = 0
for i in range(0, len(hands)):
    hand = hands[i]
    rank = i + 1
    sum += (i+1) * hand["bid"]
    print(hand["cards"], hand["rank"])
print(sum)
