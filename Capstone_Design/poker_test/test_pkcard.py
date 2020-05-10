import pytest
import random
from PA_poker_hands_in_OOP import Ranking, Hands, PKCard

non_flush_suit = 'CHSDS'
flush_suit = 'SSSSS'
test_cases = {
    Ranking.STRAIGHT_FLUSH:(
        tuple(zip('AKQJT', flush_suit)),
        tuple(zip('65432', flush_suit)),
        tuple(zip('5432A', flush_suit)),
        ),
    Ranking.FOUR_OF_A_KIND: (
        tuple(zip('AAAA4', non_flush_suit)),
        tuple(zip('2222A', non_flush_suit)),
        tuple(zip('2222K', non_flush_suit)),
        ),
    Ranking.FULL_HOUSE: (
        tuple(zip('AAAKK', non_flush_suit)),
        tuple(zip('AAATT', non_flush_suit)),
        tuple(zip('KKKAA', non_flush_suit)),
        ),
    Ranking.FLUSH: (
        tuple(zip('AQT74', flush_suit)),
        tuple(zip('A7543', flush_suit)),
        tuple(zip('J7654', flush_suit)),
        ),
    Ranking.STRAIGHT: (
        tuple(zip('AKQJT', non_flush_suit)),
        tuple(zip('65432', non_flush_suit)),
        tuple(zip('5432A', non_flush_suit)),
        ),
    Ranking.THREE_OF_A_KIND: (
        tuple(zip('AAAKJ', non_flush_suit)),
        tuple(zip('AAA32', non_flush_suit)),
        tuple(zip('TTTJ6', non_flush_suit)),
        ),
    Ranking.TWO_PAIRS: (
        tuple(zip('AA55J', non_flush_suit)),
        tuple(zip('AA554', non_flush_suit)),
        tuple(zip('55226', non_flush_suit)),
       ),
    Ranking.ONE_PAIR: (
        tuple(zip('AA432', non_flush_suit)),
        tuple(zip('KKAQJ', non_flush_suit)),
        tuple(zip('KKA54', non_flush_suit)),
      ),
    Ranking.HIGH_CARD: (
        tuple(zip('AK542', non_flush_suit)),
        tuple(zip('A7653', non_flush_suit)),
        tuple(zip('QJ752', non_flush_suit)),
        
      ),
}
def cases(*rankings):
    """get the test cases for ranking. all rankings if empty rankings
    """
    if not rankings:
        rankings = test_cases.keys()
    if rankings == ('find_kind',):
        rankings = test_cases.keys()

        return\
            [ ([r+s for r, s in case], ranking) 
                        for ranking in rankings 
                            for case in test_cases[ranking]
                                if ranking not in [Ranking.STRAIGHT_FLUSH, Ranking.STRAIGHT, Ranking.FLUSH]
            ]
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

@pytest.mark.parametrize("faces, expected", cases(Ranking.FLUSH))
def test_is_flush(faces, expected):
    origin_hand = [PKCard(c) for c in faces]
    random.shuffle(faces)
    hand = Hands([PKCard(c) for c in faces])
    result = hand.is_flush()
    assert result == True
    assert hand.cards == origin_hand

@pytest.mark.parametrize("faces, expected", cases('find_kind'))
def test_find_a_kind(faces, expected):
    origin_hand = [PKCard(c) for c in faces]
    random.shuffle(faces)
    hand = Hands([PKCard(c) for c in faces])
    result = hand.eval()
    assert result[1] == expected
    assert hand.cards == origin_hand

@pytest.mark.parametrize("faces, expected", cases())
def test_eval(faces, expected):
    origin_hand = [PKCard(c) for c in faces]
    random.shuffle(faces)
    hand = Hands([PKCard(c) for c in faces])
    result = hand.eval()
    assert result[1] == expected
    assert hand.cards == origin_hand

def test_who_wins():
    import copy
    hand_cases = [Hands(faces)for faces, ranking in cases()]
    hand_origin = copy.deepcopy(hand_cases)
    random.shuffle(hand_cases)
    for hand in hand_cases:
        hand.eval()

    for hand in hand_origin:
        hand.eval()
    sorted_cases = sorted(hand_cases, reverse = True)

    assert sorted_cases == hand_origin
    print('\nHight ot low order: ')
    for i, hand in enumerate(sorted_cases):
        print(i,hand)

def test_classify_by_rank(cTH, cJH, cQH, cKH, cAH):
    hand = Hands([cTH, cJH, cQH, cKH, cAH])
    result = hand.classify_by_rank()
    assert result == {10:[PKCard('TH')],11:[PKCard('JH')],12:[PKCard('QH')],13:[PKCard('KH')],14:[PKCard('AH')]}
