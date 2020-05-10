import pytest
from PA_poker_hands_in_OOP import PKCard

@pytest.fixture
def cAH():
    return PKCard('AH')
@pytest.fixture
def cAD():
    return PKCard('AD')
@pytest.fixture
def cAS():
    return PKCard('AS')
@pytest.fixture
def cAC():
    return PKCard('AC')

@pytest.fixture
def c2H():
    return PKCard('2H')
@pytest.fixture
def c2D():
    return PKCard('2D')
@pytest.fixture
def c2S():
    return PKCard('2S')
@pytest.fixture
def c2C():
    return PKCard('2C')

@pytest.fixture
def c3H():
    return PKCard('3H')
@pytest.fixture
def c3D():
    return PKCard('3D')
@pytest.fixture
def c3S():
    return PKCard('3S')
@pytest.fixture
def c3C():
    return PKCard('3C')

@pytest.fixture
def c4H():
    return PKCard('4H')
@pytest.fixture
def c4D():
    return PKCard('4D')
@pytest.fixture
def c4S():
    return PKCard('4S')
@pytest.fixture
def c4C():
    return PKCard('4C')

@pytest.fixture
def c5H():
    return PKCard('5H')
@pytest.fixture
def c5D():
    return PKCard('5D')
@pytest.fixture
def c5S():
    return PKCard('5S')
@pytest.fixture
def c5C():
    return PKCard('5C')

@pytest.fixture
def c6H():
    return PKCard('6H')
@pytest.fixture
def c6D():
    return PKCard('6D')
@pytest.fixture
def c6S():
    return PKCard('6S')
@pytest.fixture
def c6C():
    return PKCard('6C')

@pytest.fixture
def c7H():
    return PKCard('7H')
@pytest.fixture
def c7D():
    return PKCard('7D')
@pytest.fixture
def c7S():
    return PKCard('7S')
@pytest.fixture
def c7C():
    return PKCard('7C')

@pytest.fixture
def c8H():
    return PKCard('8H')
@pytest.fixture
def c8D():
    return PKCard('8D')
@pytest.fixture
def c8S():
    return PKCard('8S')
@pytest.fixture
def c8C():
    return PKCard('8C')

@pytest.fixture
def c9H():
    return PKCard('9H')
@pytest.fixture
def c9D():
    return PKCard('9D')
@pytest.fixture
def c9S():
    return PKCard('9S')
@pytest.fixture
def c9C():
    return PKCard('9C')

@pytest.fixture
def cTH():
    return PKCard('TH')
@pytest.fixture
def cTD():
    return PKCard('TD')
@pytest.fixture
def cTS():
    return PKCard('TS')
@pytest.fixture
def cTC():
    return PKCard('TC')

@pytest.fixture
def cJH():
    return PKCard('JH')
@pytest.fixture
def cJD():
    return PKCard('JD')
@pytest.fixture
def cJS():
    return PKCard('JS')
@pytest.fixture
def cJC():
    return PKCard('JC')

@pytest.fixture
def cQH():
    return PKCard('QH')
@pytest.fixture
def cQD():
    return PKCard('QD')
@pytest.fixture
def cQS():
    return PKCard('QS')
@pytest.fixture
def cQC():
    return PKCard('QC')

@pytest.fixture
def cKH():
    return PKCard('KH')
@pytest.fixture
def cKD():
    return PKCard('KD')
@pytest.fixture
def cKS():
    return PKCard('KS')
@pytest.fixture
def cKC():
    return PKCard('KC')

@pytest.fixture
def all_faces():
    return [r+s for r in ranks for s in suits]