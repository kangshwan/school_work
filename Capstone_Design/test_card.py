import pytest
from PA_poker_hands_in_OOP import ranks, suits, Card, PKCard

def test_PKCard_init():
    card = PKCard('AC')
    assert card.rank == 'A' and card.suit == 'C'
    assert card.card

def test_PKCard_init_exception():
    for face in ['10S', 'BD', 'TA']:
        with pytest.raises(ValueError):
            PKCard(face)

def test_PKCard_repr():
    assert repr(PKCard('AC')) == 'AC'

@pytest.fixture
def all_faces():
    return [r+s for r in ranks for s in suits]

def test_PKCard_value(all_faces):
    for face in all_faces:
        card, expected = PKCard(face), PKCard.VALUES[face[0]]
        assert card.value() == expected


def test_PKCard_comp(c9H, cJD, cJH):
    assert (cJD == cJD) and (cJD == cJH)
    assert c9H < cJD and c9H < cJD 
    assert c9H <= cJD <= cJD 
    assert c9H < cJD and c9H < cJH 
    assert cJH >= cJD >= c9H
    assert c9H != cJD and c9H != cJD 

def test_PKCard_sort(all_faces):
    all_cards = [PKCard(c) for c in all_faces]
    import random
    random.shuffle(all_cards)
    all_cards.sort()
    assert [c.value() for c in all_cards]\
        == [i for i in range(2, len(ranks)+2) for s in suits ]