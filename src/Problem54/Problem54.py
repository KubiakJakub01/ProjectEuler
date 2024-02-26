# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 14:53:33 2021

Problem 54: Poker hands
https://projecteuler.net/problem=54

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

@author: kuba
"""

PATH_TO_POKER = "poker.txt"
hands = []
with open(PATH_TO_POKER) as p:
    hands = p.readlines()

hands = [x.strip().split() for x in hands]

# player_1 = [x[:5] for x in hands]
# palyer_2 = [x[5:] for x in hands]

con_2_num = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


# Checking Straight, Flush, Straight, Royal_Flush
def check_is_straight_or_Flush(value, suit):
    if len(set(value)) == 5:
        if value[0] - value[-1] == 4:
            if len(set(suit)) == 1:
                if value[0] == 10:
                    return [10, value[-1]]
                return [9, value[-1]]
            return [5, value[-1]]
    elif len(set(suit)) == 1:
        return [6, value]
    return False


def check_is_pair(value, suit):
    unique_val = set(value)
    if len(unique_val) == 4:
        pair_of = [x for x in unique_val if value.count(x) == 2]
        return [2, pair_of + sorted(unique_val, reverse=True)]

    elif len(unique_val) == 3:
        pairs_of = [x for x in unique_val if value.count(x) == 2]
        if len(pair_of) == 2:
            return [3, pairs_of + sorted(unique_val, reverse=True)]
        else:
            pass


def check_rank_of_hand(hand):
    value = sorted([con_2_num[x[0]] for x in hand], reverse=True)
    suit = [x[1] for x in hand]
    # print('val: {} suit: {}'.format(value, suit))


def solution():
    for hand in hands[:2]:
        # player_1 = hand[:5]
        # player_2 = hand[5:]
        check_rank_of_hand(hand)


solution()
