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
    def __gt__(self, other): return self.value() >  other.value()
    def __ge__(self, other): return self.value() >= other.value()
    def __lt__(self, other): return self.value() <  other.value()
    def __le__(self, other): return self.value() <= other.value()
    def __eq__(self, other): return self.value() == other.value()
    def __ne__(self, other): return self.value() != other.value()

class PKCard(Card):
    """Card for Poker game
    """
    def value(self):
        return values[self.card[0]]
        pass



class Deck:
    

    def __init__(self, cls):
        """Create a deck of 'cls' card class
        """
        self.deck = [cls(rank+suit) for rank in ranks for suit in suits]
        pass
    
    def shuffle(self):
        import random
        random.shuffle(self.deck)
        pass

    def pop(self):
        return self.deck.pop()
        pass

    def __len__(self):
        return len(self.deck)
        pass

    def __getitem__(self, index):
        return self.deck[index]
        pass

class Hands:
    def __init__(self, cards):              # cards is list of PKCard
        temp = cards.copy()
        if len(cards) != 5:
            raise ValueError('not 5 cards')
        if type(cards[0]) == str:
            temp = []
            for card in cards:
                temp.append(PKCard(card))

        self.cards = sorted(temp, reverse=True)
        self.rank = ()
        
    def is_flush(self):
        """return: bool
        """
        if len(set(suit.suit for suit in self.cards)) == 1:
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
        rank = Ranking.HIGH_CARD
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
        return (self.cards, rank)

    def eval(self):
        """Tell the hand ranking name for the cards in hand
        
        :return: hand-ranking name
        """
        # flush, straight flush 인지 확인
        check_straight = self.is_straight() 

        if self.is_flush():
            if check_straight:
                # 스트레이트 플러시일 경우
                self.rank = (self.cards,Ranking.STRAIGHT_FLUSH)
            else:
                # 플러시일 경우
                self.rank = (self.cards, Ranking.FLUSH)
        # flush가 아니라면
        elif check_straight:
            # 스트레이트일 경우
            # No pair, one pair, two pair, three of a kind, four of a kind, full house
            self.rank =  (self.cards, Ranking.STRAIGHT)
        else:
            self.rank =  self.find_a_kind()
        return self.rank

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

    def __gt__(self, other): return self.rank[1] >  other.rank[1]
    def __ge__(self, other): return self.rank[1] >= other.rank[1]
    def __lt__(self, other): return self.rank[1] <  other.rank[1]
    def __le__(self, other): return self.rank[1] <= other.rank[1]
    def __eq__(self, other): return self.rank[1] == other.rank[1]
    def __ne__(self, other): return self.rank[1] != other.rank[1]
