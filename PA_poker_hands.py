
# coding: utf-8

# ***Jupyter Notebook에서 Download as Python으로 받으세요.***
# # PA. Find poker hands
# 포커 게임은 손에 든 패 5장을(hands라 한다) 가지고 hand의 ranking category(포커 족보)가 높은 쪽이 이기는 게임이다.
# 
# 족보에 있는지 알아 보려면, 기본적으로 다음을 check 해야 한다.
# - 5장 모두 suit이 같은지 (`is_flush`)
# - 5장 모두 rank가 연속되었는지 (`is_straight`)
# - 같은 rank가 2장인지, 3장인지, 4장인지에 따른 hand_ranking 명 (`find_a_kind)`
# 
# `tell_hand_ranking` 함수는 위 function을 이용하여 종합 판정한 결과르로
# hand rnaking name을 return해야 한다.
# 
# 아래 주어진 function들을 구현하고,
# 이들이 잘 동작함을 보여주는 test case들을 만들어 시험하고 그 결과도 제출하라.
# 
# 제출요령: VS code IDE를 이용하여 script 파일을 만들고 source와 test가 실행된 결과 화면을 zip으로 압축하여 제출한다.
# 
# 참고: [List of poker hands](http://en.wikipedia.org/wiki/List_of_poker_hands)
# - Joker는 없는 것으로 한다. 따라서 'Five of a kind'는 족보에 없다.

# 편의상 suit과 rank는 문자 하나로 표기한다. 따라서 card는 a rank와 a suit으로 구성되므로 2개의 문자나 tuple로 표현할 수 있다. 
# 그리고 sorting 편의를 위해 rank를 suit 전에 두기로 한다.
# 
# 예: '3C' 또는 ('3', 'C')

# In[ ]:


suits = 'CDHS'
ranks = '23456789TJQKA'
values = dict(zip(ranks, range(2, 2+len(ranks))))


# In[ ]:


def is_flush(cards):
    """"return: bool
    """
    pass
    
def is_straight(cards):
    """:return: the cards making flush in decreasing order if found, 
            None, otherwise
    """
    pass
    
def classify_by_rank(cards):
    """Classify the cards by ranks. 
    
    :return: dict of the form { rank: [card, ...], ...}
        None if same ranks not found
    """
    pass

def find_a_kind(cards):
    """Find if one pair, two pair, or three, four of a kind, or full house
    
    :return: hand-ranking name including 'Full house'
    """
    cards_by_ranks = classify_by_rank(cards)
    pass

def tell_hand_ranking(cards):
    """Tell the hand ranking name for the cards in hand
    
    :return: hand-ranking name
    """

if __name__ == "__main__":    # Only if this script runs as a main,
    pass                      # test code here will run.

