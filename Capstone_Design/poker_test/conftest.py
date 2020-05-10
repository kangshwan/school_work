import pytest
from PA_poker_hands_in_OOP import PKCard

@pytest.fixture
def cAH():
    return PKCard('AH')

@pytest.fixture
def c9H():
    return PKCard('9H')

@pytest.fixture
def cTH():
    return PKCard('TH')

@pytest.fixture
def cJH():
    return PKCard('JH')
@pytest.fixture
def cJD():
    return PKCard('JD')

@pytest.fixture
def cQH():
    return PKCard('QH')

@pytest.fixture
def cKH():
    return PKCard('KH')


@pytest.fixture
def all_faces():
    return [r+s for r in ranks for s in suits]