# https://adventofcode.com/2023/day/7

import functools

input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

def cardRank(card):
    ranks = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 1,
        'T': 10
    }

    return int(card) if card.isdigit() else ranks[card]

def parse(input):
    hands = []
    for line in input.split('\n')[:-1]:
        hand = {}
        rank = [0] * 15
        dealt, bid = line.split(' ')
        cards = [cardRank(card) for card in dealt]
        for card in cards:
            rank[card] += 1

        jokers = rank[1]
        rank[1] = 0
        rank = sorted(rank)[::-1][0:5]
        rank[0] += jokers

        hand["rank"] = rank + cards
        hand["cards"] = cards
        hand["bid"] = int(bid)
        hand["jokers"] = jokers
        hand["dealt"] = dealt
        hands.append(hand)
    return hands

input = open('data', 'r').read()

hands = parse(input)
hands = sorted(hands, key=lambda hand: hand["rank"])

sum = 0
for i in range(0, len(hands)):
    hand = hands[i]
    rank = i + 1
    sum += (i+1) * hand["bid"]
    print(hand["dealt"], hand["rank"], hand["jokers"])
print(sum)
