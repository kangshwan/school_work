
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

#----------straight flush----------#
# 스트레이트 + 플러시 만족.
# rolyal straight flush A K Q J 10 (가장 높음)
# steel wheel           5 4 3 2 A  (가장 낮음)
# 모양이 같다면 같은 순위.
# Q K A 2 3은 스트레이트가 아니다.(그냥 플러시)

#----------four of a kind----------#
# 같은 숫자의 카드를 4장 들고있을 경우.
# 숫자가 더 높을수록 순위가 높다.

#------------full house------------#
# three of a kind + one pair
# 같은 full house끼리 순위비교를 할 경우.
# 먼저 3페어의 숫자가 높으면 순위가 높다.
# 3페어의 숫자도 같다면, 2페어의 숫자가 높으면 순위가 높다.
# 3페어와 2페어의 숫자가 모두 같다면, 같은 순위이다.

#--------------flush---------------#
# 숫자 상관없이 5개의 카드가 모두 같은 모양일 경우.
# flush가 2명 이상일 경우, 가장 높은숫자를 비교한다.
# 가장 높은숫자가 같다면, 그 다음 높은 숫자를 비교한다.
# 모두 동일한 숫자라면, 같은 순위이다.
# flush를 만족할 경우, pair는 나올 수 없다.

#-------------straight-------------#
# 모양 상관없이 5개의 카드가 순서대로 있을경우.
# broadway straight A K Q J 10 (스트레이트에서 가장높음)
# baby straight     5 4 3 2 A  (스트레이트에서 가장 낮음)

#---------three of a kind----------#
# 5개의 핸드에서 3개의 카드가 동일한 숫자일 경우.
# 둘 다 three of a kind라면, 숫자가 높은 쪽이 순위가 높다.
# ex) 6 6 6 J A 는 3 3 3 K 2 보다 높고,
# ex) 3 3 3 K 2 는 3 3 3 J 4 보다 높다.
# 모든 숫자가 동일하다면, 같은 순위이다.

#-------------two pair-------------#
# one pair를 이룬 카드가 2개있을 경우.
# 둘 다 two pair라면, 숫자가 높은 쪽이 순위가 높다.
# ex) 10 10 2 2 K 는 5 5 4 4 10 보다 높다
# ex) 5 5 4 4 10  은 5 5 3 3 Q  보다 높다
# ex) 5 5 3 3 Q   는 5 5 3 3 J  보다 높다
# 모든 숫자가 동일하다면, 같은 순위이다.

#-------------one pair-------------#
# 같은 숫자쌍이 1개일 경우.
# 둘 다 one pair라면, 숫자가 높은 쪽이 순위가 높다.
# 9 9 Q J 5 는 6 6 K 7 4 보다 높다
# 6 6 K 7 4 는 6 6 Q J 2 보다 높다
# 6 6 Q J 2 는 6 6 Q 8 7 보다 높다

#-------------high card------------#
# 위 족보를 만족하는 경우가 없다면
# 가장 높은 숫자를 가진 쪽이 순위가 높다.

import random
suits = 'CDHS'
ranks = '23456789TJQKA'
values = dict(zip(ranks, range(2, 2+len(ranks))))
suit_dict = {'D':'Diamonds', 'C':'Clubs', 'H':'Hearts', 'S':'Spades'}
rank_dict = dict(zip('23456789', '23456789'))
rank_dict['T'], rank_dict['J'], rank_dict['Q'], rank_dict['K'], rank_dict['A'] = '10', 'Jack', 'Queen', 'King', 'Ace'
card_set = [(rank, suit)for rank in ranks for suit in suits]

def is_flush(cards):
    """"return: bool
    """
    if len(set(suit[1] for suit in cards)) == 1:
        # flush라면 카드 모양의 집합의 개수가 1일 것이다.
        return True
    else:
        # 카드 모양의 집합의 개수가 1이 아닐경우 -> flush가 아니다.
        return False
    
def is_straight(cards):
    """:return: the cards making flush in decreasing order if found, 
            None, otherwise
    """
    cards.sort(reverse = True, key=lambda t:values[t[0]])
    a_check = False                             # A는 14로 값이 책정되어있지만 A 2 3 4 5 의 예외도 있어 a_check를 만들었다/
    prev_card = values[cards[0][0]]
    answer = [cards[0]]
    if cards[0][0] == 'A':                      # 정렬된 cards에서 가장 높은 숫자가 A일 경우
        a_check = True                          # a_check은 참이된다
    for card in cards[1:]:                      # cards에서 두번째부터 탐색
        if values[card[0]] == 5 and a_check:    #두번째로 큰 수가 5이고, 가장 높은숫자가 A일경우 -> A 2 3 4 5의 가능성이 있음
            prev_card = 6                       
        if prev_card-1 == values[card[0]]:
            answer.append(card)
            prev_card = values[card[0]]
    if len(answer) == 5:
        return answer
    else:
        return None
    
def classify_by_rank(cards):
    """Classify the cards by ranks. 
    
    :return: dict of the form { rank: [card, ...], ...}
        None if same ranks not found
    """
    r_dict = {}
    for i in range(5):
        r_dict.setdefault(cards[i][0],[])
    for pair in r_dict.keys():
        r_dict[pair] = [cards[idx] for idx in range(5) if cards[idx][0] == pair]
    return r_dict

def find_a_kind(cards):
    """Find if one pair, two pair, or three, four of a kind, or full house
    
    :return: hand-ranking name including 'Full house'
    """
    cards_by_ranks = classify_by_rank(cards)       #this returns dict
    #from here sorting dict to list
    cards_by_ranks_sort = sorted(cards_by_ranks.items(), key=lambda t: values[t[0][0]], reverse = True)
    if len(cards_by_ranks) == 5:      # No pairs
        return f'{rank_dict[cards_by_ranks_sort[0][0]]} High Card'
    elif len (cards_by_ranks) == 4:   # One pairs
        for card in cards_by_ranks:
            if len(cards_by_ranks[card]) == 2:
                return f'One Pair of {rank_dict[card]}'
    elif len(cards_by_ranks) == 3:     # Thee of a Kind or Two Pair
        two_pair=[]
        for card in cards_by_ranks:
            if len(cards_by_ranks[card]) == 3:
                return f'Three of a Kind, {rank_dict[card]}'
                break
            
            if len(cards_by_ranks[card]) == 2:
                test = card
                two_pair.append(test)
        two_pair.sort(key = lambda t: values[t], reverse = True)
        return f'Two Pair, {rank_dict[two_pair[0]]} and {rank_dict[two_pair[1]]}' 
    else: # Full House or Four of a Kind
        for card in cards_by_ranks:
            if len(cards_by_ranks[card]) == 3:   #if Full House
                return f'Full House'
            elif len(cards_by_ranks[card]) == 4:    #if Four of a kind
                return f'Four of a Kind, {rank_dict[card]}'
    pass

def tell_hand_ranking(cards):
    """Tell the hand ranking name for the cards in hand
    
    :return: hand-ranking name
    """
    # flush, straight flush 인지 확인
    check_straight = is_straight(cards)

    if is_flush(cards):
        if check_straight == None:
            # 그냥 플러시일 경우
            return f"{suit_dict[cards[0][1]]} Flush"
        elif check_straight[4][0] == '2':

            return "Steel Wheel (lowest in straight flush)"
        else:
            return "Royal Straight Flush (highest in straight fulsh)"
    # flush가 아니라면
    elif check_straight == None:
        # 스트레이트도 아니라면
        # No pair, one pair, two pair, three of a kind, four of a kind, full house
        return find_a_kind(cards)
    elif check_straight[4][0] == '2' and check_straight[0][0]== 'A':
        # 카드가 A 2 3 4 5 일 경우
        return "Baby Straight (lowest in straight)"
    elif check_straight[4][0] == 'T':
        # 카드가 T J Q K A 일 경우
        return "Broadway Straight (highest in straight)"
    else:
        # 일반적인 스트레이트
        return f"{rank_dict[check_straight[0][0]]}-high Straight"

    
import sys
if __name__ == "__main__":    # Only if this script runs as a main,
    test_case=[]
    real_result = []
    test_case.append([('3','D'),('5','D'),('7','C'),('A','D'),('4','D')])
    real_result.append('Ace high card')
    test_case.append([('K','D'),('J','D'),('Q','C'),('A','D'),('T','D')])
    real_result.append('broad way straight')
    test_case.append([('4','D'),('4','C'),('4','C'),('A','S'),('A','D')])
    real_result.append('full house')
    test_case.append([('2','D'),('3','D'),('4','C'),('5','D'),('6','D')])
    real_result.append('6 high straight')
    test_case.append([('2','D'),('8','D'),('4','D'),('5','D'),('6','D')])
    real_result.append('flush')
    test_case.append([('2','D'),('2','S'),('4','H'),('J','D'),('6','D')])
    real_result.append('2 one pair')
    test_case.append([('4','D'),('A','H'),('A','C'),('A','S'),('A','D')])
    real_result.append('A four of a kind')
    test_case.append([('J', 'H'), ('2', 'S'), ('J', 'S'), ('8', 'H'), ('2', 'H')])
    real_result.append('J-2 two pairs')
    test_case.append([('6', 'H'), ('5', 'S'), ('4', 'S'), ('3', 'H'), ('2', 'H')])
    real_result.append('6 high straight')
    test_case.append([('A', 'H'), ('5', 'S'), ('4', 'S'), ('3', 'H'), ('2', 'H')])
    real_result.append('baby straight')
    test_case.append([('4','D'),('6','H'),('6','C'),('6','S'),('6','D')])
    real_result.append('6 four of a kind')
    test_case.append([('8','H'),('T','D'),('J','H'),('9','H'),('Q','H')])
    real_result.append('Q high straight')
    test_case.append([('T', 'H'), ('J', 'H'), ('K', 'H'), ('A', 'H'), ('Q', 'H')])
    real_result.append('royal straight flush')
    test_case.append([('5', 'S'), ('2', 'S'), ('A', 'S'), ('4', 'S'), ('3', 'S')])
    real_result.append('steel wheel')
    random.shuffle(card_set)
    card_idx=0
    
    for i in range(1,len(test_case)):
        print('='*100)
        print(f'\ntest case {i} card: ', test_case[i])
        print('predict rank:',real_result[i])
        print('function result:',tell_hand_ranking(test_case[i]))
        
        print()
    
    # 여기부분은 따로 카드덱을 만들어 랜덤으로 출력할 수 있는 부분입니다.
    
    """
    while(1):
        hand_card = [card for card in card_set[card_idx:card_idx+5]]
        print("\nMy card: ", hand_card)
        print(tell_hand_ranking(hand_card))
        ask = input()
        if ask in ['n','next','\\n']:
            card_idx += 5
        elif ask in ['s','stop','end','e']:
            sys.exit()

        if 52-card_idx < 5:
            print("Reset a card set....")
            random.shuffle(card_set)
            card_idx = 0
    """
    pass                      # test code here will run.


