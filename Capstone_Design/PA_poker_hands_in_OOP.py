# Constants
suits = 'CDHS'
ranks = '23456789TJQKA'
values = dict(zip(ranks, range(2,len(ranks)+2)))
from abc import ABCMeta, abstractmethod
from enum import IntEnum

class Ranking(IntEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8

class Card(metaclass=ABCMeta):
    """Abstact class for playing cards
    """
    VALUES = values
    def __init__(self, rank_suit):
        if rank_suit[0] not in ranks or rank_suit[1] not in suits:
            raise ValueError(f'{rank_suit}: illegal card')
        self.card = rank_suit
        self.rank = rank_suit[0]
        self.suit = rank_suit[1]
        
    def __repr__(self):
        return self.card
    
    @abstractmethod
    def value(self):
        """Subclasses should implement this method
        """
        raise NotImplementedError("value method not implemented")

    # card comparison operators
    def __gt__(self, other): return self.value() > other.value()
    def __ge__(self, other): return self.value() >= other.value()
    def __lt__(self, other): return self.value() < other.value()
    def __le__(self, other): return self.value() <= other.value()
    def __eq__(self, other): return self.value() == other.value()
    def __ne__(self, other): return self.value() != other.value()

class PKCard(Card):
    """Card for Poker game
    """
    def value(self):
        return values[self.card[0]]
        pass

    def suit(self):         # 이 함수는 카드의 모양을 리턴해줍니다.
        return self.card[1]

import random

class Deck:
    def __init__(self, cls):
        """Create a deck of 'cls' card class
        """
        self.deck = [cls(rank+suit) for rank in ranks for suit in suits]
        pass
    
    def shuffle(self):
        random.shuffle(self.deck)
        pass

    def pop(self):
        return self.deck.pop()
        pass

    def __str__(self):
        return str(self.deck)
        pass

    def __len__(self):
        return len(self.deck)
        pass

    def __getitem__(self, index):
        return self.deck[index]
        pass

class Hands:
    def __init__(self, cards):              # cards is list of PKCard
        if len(cards) != 5:
            raise ValueError('not 5 cards')
        self.cards = sorted(cards, reverse=True)
        self.rank = ()
    def is_flush(self):
        """return: bool
        """
        if len(set(suit.suit() for suit in self.cards)) == 1:
            # flush라면 카드 모양의 집합의 개수가 1일 것이다.
            return True
        else:
            # 카드 모양의 집합의 개수가 1이 아닐경우 -> flush가 아니다.
            return False

    def is_straight(self):      # Hand class
        """:return: the cards making flush in decreasing order if found, 
                None, otherwise
        """
        a_high = False                              # A는 14로 값이 책정되어있지만 A 2 3 4 5 의 예외도 있어 a_check를 만들었다
        answer = [self.cards[0]]
        prev_value = (self.cards[0]).value()

        if str(self.cards[0])[0] == 'A':            # 정렬된 cards에서 가장 높은 숫자가 A일 경우
            a_high = True                           # a_check은 참이된다
        for card in self.cards[1:]:                 # cards에서 두번째부터 탐색
            if card.value() == 5 and a_high:        # 두번째로 큰 수가 5이고, 가장 높은숫자가 A일경우 -> A 2 3 4 5의 가능성이 있음
                prev_value = 6
            if prev_value-1 == card.value():
                answer.append(card)
                prev_value = card.value()
        if len(answer) == 5:
            if answer[0].value() == 14 and answer[1].value() == 5 :    # A가 가장 작은수로 쓰이는 경우
                temp = []
                for i in answer[1:]:
                    temp.append(i)
                temp.append(answer[0])
                self.cards = temp
            return True
        return False

    def classify_by_rank(self):
        """Classify the cards by ranks. 
        
        :return: dict of the form { rank: [card, ...], ...}
            None if same ranks not found
        """
        self.r_dict = {}
        for i in range(5):
            self.r_dict.setdefault(self.cards[i].value(),[])
        for pair in self.r_dict.keys():
            self.r_dict[pair] = [self.cards[idx] for idx in range(5) if self.cards[idx].value() == pair]
        return self.r_dict

    def find_a_kind(self):
        """Find if one pair, two pair, or three, four of a kind, or full house
        
        :return: hand-ranking name including 'Full house'
        """
        cards_by_ranks = self.classify_by_rank()       # this returns dict
        #from here sorting dict to list
        rank = 0
        cards = []
        if len(cards_by_ranks) == 5:        # No pairs
            cards = self.cards              # rank 0 for no pair(high card)

        elif len (cards_by_ranks) == 4:     # One pairs
            for card in cards_by_ranks:     
                if len(cards_by_ranks[card]) == 2:
                    rank = Ranking.ONE_PAIR                # rank 1 for one pair
                    cards+=cards_by_ranks[card]
            # 나머지를 cards에 넣어준다.
            for card in cards_by_ranks:
                if len(cards_by_ranks[card]) != 2:
                    cards += cards_by_ranks[card]
        elif len(cards_by_ranks) == 3:      # Thee of a Kind or Two Pair
            for card in cards_by_ranks:
                if len(cards_by_ranks[card]) == 3:
                    rank = Ranking.THREE_OF_A_KIND                # rank 3 for Three of a kind
                    cards += cards_by_ranks[card]
                    break
                if len(cards_by_ranks[card]) == 2:
                    rank = Ranking.TWO_PAIRS                # rank 2 for two pairs
                    cards += cards_by_ranks[card]
            for card in cards_by_ranks:
                if len(cards_by_ranks[card]) != 2 and len(cards_by_ranks[card])!= 3:
                    cards += cards_by_ranks[card]       
        else: # Full House or Four of a Kind
            for card in cards_by_ranks:
                if len(cards_by_ranks[card]) == 3:      # if Full House
                    rank = Ranking.FULL_HOUSE                            # rank 6 for full house
                    cards += cards_by_ranks[card]
                    break
                if len(cards_by_ranks[card]) == 4:    # if Four of a kind
                    rank = Ranking.FOUR_OF_A_KIND                            # rank 7 for four of a kind
                    cards += cards_by_ranks[card]
            for card in cards_by_ranks:
                if len(cards_by_ranks[card]) != 3 and len(cards_by_ranks[card])!= 4:
                    cards += cards_by_ranks[card]

        self.cards = cards
        return (rank, self.cards)

    def eval(self):
        """Tell the hand ranking name for the cards in hand
        
        :return: hand-ranking name
        """
        # flush, straight flush 인지 확인
        check_straight = self.is_straight() 

        if self.is_flush():
            if check_straight:
                # 스트레이트 플러시일 경우
                self.rank = (8, self.cards)
            else:
                # 플러시일 경우
                self.rank = (5, self.cards)
        # flush가 아니라면
        elif self.is_straight():
            # 스트레이트일 경우
            # No pair, one pair, two pair, three of a kind, four of a kind, full house
            self.rank =  (4, self.cards)
        else:
            self.rank =  self.find_a_kind()

    def is_win(self, other):
        self.eval()
        other.eval()
        #-----main문에서 카드 값을 비교하는것이 힘들어 여기서 출력합니다.-----#
        print(self.rank)
        print(other.rank)
        if self.rank[0]> other.rank[0]:      # rank 가 더 높을경우
            return True
        elif self.rank[0] < other.rank[0]:   # rank 가 더 낮을경우
            return False
        else:                               # rank가 같을 경우
            for (mine, your) in zip(self.rank[1], other.rank[1]):
                if mine > your:
                    return True
                elif mine < your:
                    return False
                else:
                    pass
        return None

    def __str__(self):
        return str(self.cards)

rank_name = ['High card','One pair', 'Two Pair', 'Three of a kind', 'Straight', 'Flush', 'Full house', 'Four of a kind', 'Straight flush']
rank_dict = dict(zip(range(9),rank_name))

import os

import sys
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.\n".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.\n".format(linenum))
    print(msg)
deck = Deck(PKCard)
deck.shuffle()
deck.pop()
test_cases=[]
"""
test_cases  0~3  : high card
test_cases  4~7  : one pair
test_cases  8~12 : two pair
test_cases 13~14 : three of a kind
test_cases 15~18 : straight
test_cases 19~22 : Flush
test_cases 23~25 : Full house
test_cases 26~28 : Four of a kind
test_cases 28~31 : Straight flush

"""
# case for high card
test_cases.append(Hands([PKCard('3D'), PKCard('5D'), PKCard('7C'), PKCard('AD'), PKCard('4D')]))
test_cases.append(Hands([PKCard('JS'), PKCard('5C'), PKCard('7H'), PKCard('2D'), PKCard('4H')]))
test_cases.append(Hands([PKCard('5H'), PKCard('3H'), PKCard('7D'), PKCard('JD'), PKCard('4S')]))
test_cases.append(Hands([PKCard('JC'), PKCard('5S'), PKCard('7S'), PKCard('3S'), PKCard('4C')]))

# case for one pair
test_cases.append(Hands([PKCard('2S'), PKCard('AS'), PKCard('4H'), PKCard('5H'), PKCard('AH')])) 
test_cases.append(Hands([PKCard('2C'), PKCard('3H'), PKCard('7S'), PKCard('TC'), PKCard('TH')]))
test_cases.append(Hands([PKCard('2S'), PKCard('4D'), PKCard('7H'), PKCard('TD'), PKCard('TS')]))
test_cases.append(Hands([PKCard('2D'), PKCard('7C'), PKCard('4H'), PKCard('TC'), PKCard('TH')]))

# case for two pair
test_cases.append(Hands([PKCard('JH'), PKCard('2S'), PKCard('JS'), PKCard('8H'), PKCard('2H')]))
test_cases.append(Hands([PKCard('JD'), PKCard('AS'), PKCard('JC'), PKCard('8S'), PKCard('AH')]))
test_cases.append(Hands([PKCard('TH'), PKCard('AD'), PKCard('TS'), PKCard('8H'), PKCard('AC')]))
test_cases.append(Hands([PKCard('TD'), PKCard('AH'), PKCard('TC'), PKCard('7H'), PKCard('AS')]))
test_cases.append(Hands([PKCard('TH'), PKCard('AD'), PKCard('TS'), PKCard('7S'), PKCard('AC')]))

# case for three of a kind
# 3개의 카드가 두명에게 동시에 같은숫자가 있는것은 불가능하다.
# ex) TD TS TH JD 6D 
#     TC TD TS JC 5C
# 는 불가능 하므로, 비교대상에서 제외.
# 따라서 같은 비길 수도 없음.
# 두 핸드가 서로 Three of a kind라면, 둘중 하나는 이기고 진다.
test_cases.append(Hands([PKCard('TD'), PKCard('TS'), PKCard('TH'), PKCard('JD'), PKCard('6D')]))
test_cases.append(Hands([PKCard('4D'), PKCard('4S'), PKCard('4H'), PKCard('AD'), PKCard('6D')]))

# case for straight
test_cases.append(Hands([PKCard('AH'), PKCard('JD'), PKCard('KS'), PKCard('TD'), PKCard('QS')]))
test_cases.append(Hands([PKCard('AD'), PKCard('JS'), PKCard('KC'), PKCard('TS'), PKCard('QH')]))
test_cases.append(Hands([PKCard('2H'), PKCard('3D'), PKCard('4S'), PKCard('5D'), PKCard('6S')]))
test_cases.append(Hands([PKCard('2C'), PKCard('3S'), PKCard('4C'), PKCard('5S'), PKCard('AS')]))


# case for flush
test_cases.append(Hands([PKCard('3D'), PKCard('5D'), PKCard('7D'), PKCard('AD'), PKCard('4D')]))
test_cases.append(Hands([PKCard('JS'), PKCard('5S'), PKCard('7S'), PKCard('2S'), PKCard('4S')]))
test_cases.append(Hands([PKCard('5C'), PKCard('6C'), PKCard('7C'), PKCard('JC'), PKCard('4C')]))
test_cases.append(Hands([PKCard('JH'), PKCard('5H'), PKCard('7H'), PKCard('6H'), PKCard('4H')])) 

# case for full house
# three of a kind 와 동일하게 같은 수의 카드쌍이 나올 수 없다.
# full house끼리도 역시 동점은 나올 수 없음.
test_cases.append(Hands([PKCard('4D'), PKCard('4C'), PKCard('4S'), PKCard('AS'), PKCard('AD')]))
test_cases.append(Hands([PKCard('5D'), PKCard('5C'), PKCard('5S'), PKCard('2H'), PKCard('2C')]))

# case for four of a kind
# four of a kind끼리도 역시 동점이 나올 수 없다.
test_cases.append(Hands([PKCard('4D'), PKCard('AH'), PKCard('AC'), PKCard('AS'), PKCard('AD')]))
test_cases.append(Hands([PKCard('9D'), PKCard('JH'), PKCard('JC'), PKCard('JS'), PKCard('JD')]))
test_cases.append(Hands([PKCard('AD'), PKCard('2H'), PKCard('2C'), PKCard('2S'), PKCard('2D')]))

# case for straight flush
test_cases.append(Hands([PKCard('2D'), PKCard('3D'), PKCard('4D'), PKCard('5D'), PKCard('6D')]))
test_cases.append(Hands([PKCard('AH'), PKCard('JH'), PKCard('KH'), PKCard('TH'), PKCard('QH')]))
test_cases.append(Hands([PKCard('AS'), PKCard('JS'), PKCard('KS'), PKCard('TS'), PKCard('QS')]))
test_cases.append(Hands([PKCard('2C'), PKCard('3C'), PKCard('4C'), PKCard('5C'), PKCard('AC')]))



# None means that two cards are equal.

print('='*30)
print('Test cases for High Card')
print('='*30)
test(test_cases[0].is_win(test_cases[1]) == True)       
test(test_cases[1].is_win(test_cases[2]) == False)
test(test_cases[2].is_win(test_cases[3]) == None)

print()
print('='*30)
print('Test cases for One Pair')
print('='*30)
test(test_cases[4].is_win(test_cases[5]) == True)
test(test_cases[5].is_win(test_cases[6]) == False)
test(test_cases[6].is_win(test_cases[7]) == None)

print()
print('='*30)
print('Test cases for Two Pair')
print('='*30)
test(test_cases[8].is_win(test_cases[9]) == False)
test(test_cases[9].is_win(test_cases[10]) == True)
test(test_cases[10].is_win(test_cases[11]) == True)
test(test_cases[11].is_win(test_cases[12]) == None)

print()
print('='*30)
print('Test cases for Three of a kind')
print('='*30)
test(test_cases[13].is_win(test_cases[14]) == True)

print()
print('='*30)
print('Test cases for Straight')
print('='*30)
test(test_cases[15].is_win(test_cases[16]) == None)
test(test_cases[16].is_win(test_cases[17]) == True)
test(test_cases[17].is_win(test_cases[18]) == True)

print()
print('='*30)
print('Test cases for Flush')
print('='*30)    
test(test_cases[19].is_win(test_cases[20]) == True)       
test(test_cases[20].is_win(test_cases[21]) == False)
test(test_cases[21].is_win(test_cases[22]) == None)

print()
print('='*30)
print('Test cases for Full House')
print('='*30) 
test(test_cases[23].is_win(test_cases[24]) == False)       

print()
print('='*30)
print('Test cases for Four of a kind')
print('='*30) 
test(test_cases[25].is_win(test_cases[26]) == True)
test(test_cases[26].is_win(test_cases[27]) == True)

print()
print('='*30)
print('Test cases for Straight Flush')
print('='*30) 
test(test_cases[28].is_win(test_cases[29]) == False)
test(test_cases[29].is_win(test_cases[30]) == None)
test(test_cases[30].is_win(test_cases[31]) == True)

print()
print('='*30)
print('Test cases for Different Ranks')
# 아래부터 나오는 test case는 단순 rank 비교를 하는것입니다.
print('='*30) 
test(test_cases[0].is_win(test_cases[4]) == False)
test(test_cases[0].is_win(test_cases[8]) == False)
test(test_cases[0].is_win(test_cases[13]) == False)
test(test_cases[0].is_win(test_cases[15]) == False)
test(test_cases[0].is_win(test_cases[19]) == False)
test(test_cases[0].is_win(test_cases[23]) == False)
test(test_cases[0].is_win(test_cases[26]) == False)
test(test_cases[0].is_win(test_cases[28]) == False)

print()
print('='*30)
test(test_cases[4].is_win(test_cases[0]) == True)
test(test_cases[4].is_win(test_cases[9]) == False)
test(test_cases[4].is_win(test_cases[14]) == False)
test(test_cases[4].is_win(test_cases[16]) == False)
test(test_cases[4].is_win(test_cases[20]) == False)
test(test_cases[4].is_win(test_cases[24]) == False)
test(test_cases[4].is_win(test_cases[27]) == False)
test(test_cases[4].is_win(test_cases[29]) == False)

print()
print('='*30)
test(test_cases[8].is_win(test_cases[1]) == True)
test(test_cases[8].is_win(test_cases[5]) == True)
test(test_cases[8].is_win(test_cases[13]) == False)
test(test_cases[8].is_win(test_cases[17]) == False)
test(test_cases[8].is_win(test_cases[21]) == False)
test(test_cases[8].is_win(test_cases[25]) == False)
test(test_cases[8].is_win(test_cases[26]) == False)
test(test_cases[8].is_win(test_cases[30]) == False)

print()
print('='*30)
test(test_cases[13].is_win(test_cases[2]) == True)
test(test_cases[13].is_win(test_cases[6]) == True)
test(test_cases[13].is_win(test_cases[9]) == True)
test(test_cases[13].is_win(test_cases[15]) == False)
test(test_cases[13].is_win(test_cases[22]) == False)
test(test_cases[13].is_win(test_cases[23]) == False)
test(test_cases[13].is_win(test_cases[27]) == False)
test(test_cases[13].is_win(test_cases[28]) == False)

print()
print('='*30)
test(test_cases[15].is_win(test_cases[3]) == True)
test(test_cases[15].is_win(test_cases[7]) == True)
test(test_cases[15].is_win(test_cases[10]) == True)
test(test_cases[15].is_win(test_cases[14]) == True)
test(test_cases[15].is_win(test_cases[19]) == False)
test(test_cases[15].is_win(test_cases[24]) == False)
test(test_cases[15].is_win(test_cases[26]) == False)
test(test_cases[15].is_win(test_cases[29]) == False)

print()
print('='*30)
test(test_cases[19].is_win(test_cases[0]) == True)
test(test_cases[19].is_win(test_cases[4]) == True)
test(test_cases[19].is_win(test_cases[11]) == True)
test(test_cases[19].is_win(test_cases[13]) == True)
test(test_cases[19].is_win(test_cases[16]) == True)
test(test_cases[19].is_win(test_cases[25]) == False)
test(test_cases[19].is_win(test_cases[27]) == False)
test(test_cases[19].is_win(test_cases[30]) == False)

print()
print('='*30)
test(test_cases[23].is_win(test_cases[1]) == True)
test(test_cases[23].is_win(test_cases[5]) == True)
test(test_cases[23].is_win(test_cases[12]) == True)
test(test_cases[23].is_win(test_cases[14]) == True)
test(test_cases[23].is_win(test_cases[17]) == True)
test(test_cases[23].is_win(test_cases[20]) == True)
test(test_cases[23].is_win(test_cases[26]) == False)
test(test_cases[23].is_win(test_cases[28]) == False)

print()
print('='*30)
test(test_cases[26].is_win(test_cases[2]) == True)
test(test_cases[26].is_win(test_cases[6]) == True)
test(test_cases[26].is_win(test_cases[8]) == True)
test(test_cases[26].is_win(test_cases[13]) == True)
test(test_cases[26].is_win(test_cases[15]) == True)
test(test_cases[26].is_win(test_cases[21]) == True)
test(test_cases[26].is_win(test_cases[23]) == True)
test(test_cases[26].is_win(test_cases[29]) == False)

print()
print('='*30)
test(test_cases[28].is_win(test_cases[2]) == True)
test(test_cases[28].is_win(test_cases[6]) == True)
test(test_cases[28].is_win(test_cases[8]) == True)
test(test_cases[28].is_win(test_cases[13]) == True)
test(test_cases[28].is_win(test_cases[15]) == True)
test(test_cases[28].is_win(test_cases[21]) == True)
test(test_cases[28].is_win(test_cases[23]) == True)
test(test_cases[28].is_win(test_cases[27]) == True)

# your test cases here
pass