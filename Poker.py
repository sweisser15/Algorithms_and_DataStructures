# File: Poker.py

# Description: Virtual Poker

import random

class Card(object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    SUITS = ('C', 'D', 'H', 'S')

    # constructor
    def __init__(self, rank=12, suit='S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12

        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    # string representation of a Card object
    def __str__(self):
        if (self.rank == 14):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str(self.rank)
        return rank + self.suit

    # equality tests
    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank


class Deck(object):
    # constructor
    def __init__(self, num_decks=1):
        self.deck = []
        for i in range(num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card(rank, suit)
                    self.deck.append(card)

    # shuffle the deck
    def shuffle(self):
        random.shuffle(self.deck)

    # deal a card
    def deal(self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)


class Poker(object):
    # constructor
    def __init__(self, num_players=2, num_cards=5):
        self.deck = Deck()
        self.deck.shuffle()
        self.all_hands = []
        self.numCards_in_Hand = num_cards

        # deal the cards to the players
        for i in range(num_players):
            hand = []
            for j in range(self.numCards_in_Hand):
                hand.append(self.deck.deal())
            self.all_hands.append(hand)

    # simulate the play of poker
    def play(self):

        # sort the hands of each player and print
        for i in range(len(self.all_hands)):
            sorted_hand = sorted (self.all_hands[i], reverse = True)
            self.all_hands[i] = sorted_hand
            hand_str = ''
            for card in reversed(sorted_hand):
                hand_str = hand_str + str(card) + ' '
            print('Player ' + str(i + 1) + ' : ' + hand_str)

        # determine the type of each hand and print
    # determine winner and print

    # determine if a hand is a royal flush
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand, and the rank of a royal flush
    def is_royal(self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''

        rank_order = True
        for i in range(len(hand)):
            rank_order = rank_order and (hand[i].rank == 10 + i)

        if (not rank_order):
            return 0, ''

        points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Royal Flush', 10

    #determines if a hand is a straight flush
    #returns the rank of a straight flush and the points of the hand
    def is_straight_flush (self, hand):
        same_suit = True
        for i in range(len(hand)-1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''

        rank_order = True
        for i in range(len(hand)-1):
            rank_order = rank_order and (hand[i].rank == int(hand[i+1].rank - 1))

        if (not rank_order):
            return 0, ''

        points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight Flush', 9

    #determines if hand is a four of a kind
    #returns the rank of a four of a kind and the points of the hand
    def is_four_kind (self, hand):
        if  (hand[0].rank == hand[3].rank):

            points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[0].rank) * 15 ** 3
            points = points + (hand[0].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
            points = points + (hand[4].rank)

            return points, 'Four of a Kind', 8

        elif (hand[1].rank == hand[4].rank):

            points = 8 * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
            points = points + (hand[1].rank) * 15 ** 2 + (hand[1].rank) * 15 ** 1
            points = points + (hand[0].rank)


            return points, 'Four of a Kind', 8

        else:
            return 0, ''

    #determines if the hand is a full house
    #returns the rank of a full house and the points of the hand
    def is_full_house (self, hand):
        if ((hand[0].rank == hand[2].rank) and (hand[3].rank == hand[4].rank)):

            points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[0].rank) * 15 ** 3
            points = points + (hand[0].rank) * 15 ** 2 + (hand[4].rank) * 15 ** 1
            points = points + (hand[4].rank)

            return points, 'Full House', 7

        elif ((hand[0].rank == hand[1].rank) and (hand[2].rank == hand[4].rank)):

            points = 7 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3
            points = points + (hand[2].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
            points = points + (hand[0].rank)

            return points, 'Full House', 7

        else:
            return 0, ''

    #determines if the hand is a flush
    #returns the rank and the points of the hand
    def is_flush (self, hand):
        same_suit = True
        for i in range(len(hand)-1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''

        points = 6 * 15 ** 5 + (hand[4].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[1].rank) * 15 ** 1
        points = points + (hand[0].rank)

        return points, 'Flush', 6

    #determines if the hand is straight
    #returns the rank of a straight and the points of the hand
    def is_straight (self, hand):
        rank_order = True
        for i in range(len(hand)-1):
            rank_order = rank_order and (hand[i].rank == int(hand[i+1].rank - 1))

        if (not rank_order):
            return 0, ''

        points = 5 * 15 ** 5 + (hand[4].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[1].rank) * 15 ** 1
        points = points + (hand[0].rank)

        return points, 'Straight', 5

    #determines if the hand is a three of a kind
    #returns the rank of a three of a kind and the points of the hand
    def is_three_kind (self, hand):
        if (hand[0].rank == hand[2].rank):

            points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[0].rank) * 15 ** 3
            points = points + (hand[0].rank) * 15 ** 2 + (hand[4].rank) * 15 ** 1
            points = points + (hand[3].rank)

            return points, 'Three of a Kind', 4

        elif (hand[1].rank == hand[3].rank):

            points = 4 * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
            points = points + (hand[1].rank) * 15 ** 2 + (hand[4].rank) * 15 ** 1
            points = points + (hand[0].rank)

            return points, 'Three of a Kind', 4

        elif (hand[2].rank == hand[4].rank):

            points = 4 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3
            points = points + (hand[2].rank) * 15 ** 2 + (hand[1].rank) * 15 ** 1
            points = points + (hand[0].rank)

            return points, 'Three of a Kind', 4

        else:
            return 0, ''

    #determines if the hand is a two pair
    #returns the rank of a two pair and the points of the hand
    def is_two_pair (self, hand):
        if hand[0].rank == hand[1].rank and (hand[2].rank == hand[3].rank):

            points = 3 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3
            points = points + (hand[0].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
            points = points + (hand[4].rank)

            return points, 'Two Pair', 3

        elif hand[0].rank == hand[1].rank and (hand[3].rank == hand[4].rank):

            points = 3 * 15 ** 5 + (hand[3].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3
            points = points + (hand[0].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
            points = points + (hand[2].rank)

            return points, 'Two Pair', 3

        elif (hand[1].rank == hand[2].rank and hand[3].rank == hand[4].rank):

            points = 3 * 15 ** 5 + (hand[3].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3
            points = points + (hand[1].rank) * 15 ** 2 + (hand[1].rank) * 15 ** 1
            points = points + (hand[0].rank)

            return points, 'Two Pair', 3


        else:
            return 0, ''

    # determine if a hand is one pair
    # takes as argument a list of 5 Card objects
    # returns the number of points for that hand
    def is_one_pair (self, hand):
        one_pair = False
        for i in range (len(hand) - 1):
          if (hand[i].rank == hand[i + 1].rank):
            locPair = i
            valPair = hand[i].rank
            one_pair = True
        if (not one_pair):
              return 0, ''
        tempHand = hand.copy()
        tempHand.pop(locPair)
        tempHand.pop(locPair)

        points = 2 * 15 ** 5 + (valPair) * 15 ** 4 + (valPair) * 15 ** 3
        points = points + (tempHand[2].rank) * 15 ** 2 + (tempHand[1].rank) * 15 ** 1
        points = points + (tempHand[0].rank)

        return points, 'One Pair', 2

    #determines the points of the hand if it matches no other type of hand
    #returns points of the hand and the rank
    def is_high_card(self, hand):

        points = 1 * 15 ** 5 + (hand[4].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[1].rank) * 15 ** 1
        points = points + (hand[0].rank)

        return points, 'High Card', 1


def main():
    # prompt the user to enter the number of plaers
    num_players = int(input('Enter number of players: '))
    print("")
    while ((num_players < 2) or (num_players > 6)):
        num_players = int(input('Enter number of players: '))

    # create the Poker object
    game = Poker(num_players)

    # play the game
    game.play()
    hand_type = []
    hand_points = []

    #once the type of hand is determined, it is not considered for other types
    hand_flag = [True] * num_players
    for i in range(num_players):
        currentHand = game.all_hands[i]
        myList = game.is_royal(currentHand)
        if int(myList[0]) > 0:
            hand_type.append([i + 1, myList[1]])
            hand_points.append([i + 1, myList[0], myList[2]])
            hand_flag[i] = False
        myList = game.is_straight_flush(currentHand)
        if (int(myList[0]) > 0) and (hand_flag[i] == True):
            hand_type.append([i + 1, myList[1]])
            hand_points.append([i + 1, myList[0], myList[2]])
            hand_flag[i] = False
        myList = game.is_four_kind(currentHand)
        if (int(myList[0]) > 0) and (hand_flag[i] == True):
            hand_type.append([i + 1, myList[1]])
            hand_points.append([i + 1, myList[0], myList[2]])
            hand_flag[i] = False
        myList = game.is_full_house(currentHand)
        if (int(myList[0]) > 0) and (hand_flag[i] == True):
            hand_type.append([i + 1, myList[1]])
            hand_points.append([i + 1, myList[0], myList[2]])
            hand_flag[i] = False
        myList = game.is_flush(currentHand)
        if (int(myList[0]) > 0) and (hand_flag[i] == True):
            hand_type.append([i + 1, myList[1]])
            hand_points.append([i + 1, myList[0], myList[2]])
            hand_flag[i] = False
        myList = game.is_straight(currentHand)
        if (int(myList[0]) > 0) and (hand_flag[i] == True):
            hand_type.append([i + 1, myList[1]])
            hand_points.append([i + 1, myList[0], myList[2]])
            hand_flag[i] = False
        myList = game.is_three_kind(currentHand)
        if (int(myList[0]) > 0) and (hand_flag[i] == True):
            hand_type.append([i + 1, myList[1]])
            hand_points.append([i + 1, myList[0], myList[2]])
            hand_flag[i] = False
        myList = game.is_two_pair(currentHand)
        if (int(myList[0]) > 0) and (hand_flag[i] == True):
            hand_type.append([i + 1, myList[1]])
            hand_points.append([i + 1, myList[0], myList[2]])
            hand_flag[i] = False
        myList = game.is_one_pair(currentHand)
        if (int(myList[0]) > 0) and (hand_flag[i] == True):
            hand_type.append([i + 1, myList[1]])
            hand_points.append([i + 1, myList[0], myList[2]])
            hand_flag[i] = False
        myList = game.is_high_card(currentHand)
        if (int(myList[0]) > 0) and (hand_flag[i] == True):
            hand_type.append([i + 1, myList[1]])
            hand_points.append([i + 1, myList[0], myList[2]])
            hand_flag[i] = False

    print("")
    for i in range(len(hand_type)):
        print("Player " + str(i + 1) + ": " + str(hand_type[i][1]))
    print("")

    #reverse the players hand so it is in descending order of rank, followed by points
    hand_points = sorted(hand_points, key=lambda x:(x[2], x[1]), reverse=True)

    #determines the winner by making sure the highest rank is not equal to the
    #second highest rank
    if hand_points[0][2] > hand_points[1][2]:
            print("Player " + str(hand_points[0][0]) + " wins.")

    #the first player in hand points always wins the tie since it is
    #in descending order of points
    else:
        print("Player " + str(hand_points[0][0]) + " ties.")

    for i in range(1,len(hand_points)):
        if hand_points[i][2] == hand_points[0][2]:
            print("Player " + str(hand_points[i][0]) + " ties.")

main()




