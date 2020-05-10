import pytest
import random
from PA_poker_hands_in_OOP import Ranking, Hands, PKCard

non_flush_suit = 'CHSDS'
flush_suit = 'SSSSS'
test_cases = {
    Ranking.STRAIGHT_FLUSH:(
        tuple(zip('65432', flush_suit)),
        tuple(zip('AJKQJ', flush_suit)),
        tuple(zip('2345A', flush_suit)),
        ),
    Ranking.FOUR_OF_A_KIND: (
        tuple(zip('4AAAA', non_flush_suit)),
        tuple(zip('2222A', non_flush_suit)),
        tuple(zip('2222K', non_flush_suit)),
        ),
    Ranking.FULL_HOUSE: (
        tuple(zip('KKKAA', non_flush_suit)),
        tuple(zip('AAAKK', non_flush_suit)),
        tuple(zip('AAATT', non_flush_suit)),
        ),
    Ranking.FLUSH: (
        tuple(zip('537A4', flush_suit)),
        tuple(zip('A74TQ', flush_suit)),
        tuple(zip('J5764', flush_suit)),
        ),
    Ranking.STRAIGHT: (
        tuple(zip('65432', non_flush_suit)),
        tuple(zip('AKQJT', non_flush_suit)),
        tuple(zip('5432A', non_flush_suit)),
        ),
    Ranking.THREE_OF_A_KIND: (
        tuple(zip('TTTJ6', non_flush_suit)),
        tuple(zip('AAA23', non_flush_suit)),
        tuple(zip('AAAJK', non_flush_suit)),
        ),
    Ranking.TWO_PAIRS: (
        tuple(zip('22556', non_flush_suit)),
        tuple(zip('55AAJ', non_flush_suit)),
        tuple(zip('AA545', non_flush_suit)),
       ),
    Ranking.ONE_PAIR: (
        tuple(zip('234AA', non_flush_suit)),
        tuple(zip('AKKQJ', non_flush_suit)),
        tuple(zip('AKK45', non_flush_suit)),
      ),
    Ranking.HIGH_CARD: (
        tuple(zip('6375A', non_flush_suit)),
        tuple(zip('5J7Q2', non_flush_suit)),
        tuple(zip('K245A', non_flush_suit)),
      ),
}
def cases(*rankings):
    """get the test cases for ranking. all rankings if empty rankings
    """
    if not rankings:
        rankings = test_cases.key()
    return \
        [ ([r+s for r, s in case], ranking)
                    for ranking in rankings
                        for case in test_cases[ranking]
        ]

@pytest.mark.parametrize("faces, expected", cases(Ranking.STRAIGHT))
def test_is_straight(faces, expected):
    origin_hand = [PKCard(c) for c in faces]
    random.shuffle(faces)
    hand = Hands([PKCard(c) for c in faces])
    result = hand.is_straight()
    assert result == True
    assert hand.cards == origin_hand

@pytest.mark.parametrize("faces, expected", cases())
def test_find_a_kind(faces, expected):
    pass