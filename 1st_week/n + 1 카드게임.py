# https://school.programmers.co.kr/learn/courses/30/lessons/258707

"""
## 알아야할 함수 ##
1. list.index("찾을 값") -> 특정 값의 index 반환

## 특이사항 ##
점수 : 15/100

##################
"""

def check_num(cur_card,friend_idx,cur_range):
    able_num = 0
    able_friends = []
    coin_cost_array = []
    cur_friend_idx = friend_idx[:cur_range]
    for idx, friend in enumerate(cur_friend_idx):
        if idx != -1 and friend != -1 and friend > idx and friend < cur_range:
            able_num += 1
            able_friends.append([idx,friend])
            if (idx >= 4 and friend < 4) or (idx < 4 and friend >= 4):
                coin_cost_array.append(1)
            elif (idx >= 4 and friend >= 4):
                coin_cost_array.append(2)
            else :
                coin_cost_array.append(0)
            
    return able_num, able_friends, coin_cost_array

def solution(coin, cards):
    max_num = len(cards)
    max_round_num = (max_num - 4)//2 + 1
    print(f'max_round_num : {max_round_num}')
    
    friend_idx = [0]*len(cards)
    for i in range(len(cards)):
        friend_idx[i] = cards.index(max_num + 1 - (cards[i]))
    
    cur_card = cards[:4]
    
    for round_num in range(1 , max_round_num):
        next_card = cards[(round_num-1)*2+4:(round_num)*2+4]
        cur_card = cur_card + next_card
        
        cur_friend_idx = [-1]*len(cur_card)
        for i in range(len(cur_card)):
            if max_num + 1 - (cur_card[i]) in cur_card:
                cur_friend_idx[i] = cur_card.index(max_num + 1 - (cur_card[i]))
        
        print('********')
        print(f'round_num : {round_num}')
        print(f'cur_card : {cur_card}')
        print(f'cur_friend_idx : {cur_friend_idx}')
        cur_range = 4 + round_num*2

        able_num, able_friends, coin_cost_array = check_num(cur_card,cur_friend_idx,cur_range)
        print(f'able_friends : {able_friends}')
        if able_friends:
            prior_set = -1
            if 0 in coin_cost_array:
                prior_set = coin_cost_array.index(0)
            elif 1 in coin_cost_array:
                prior_set = coin_cost_array.index(1)
                coin -= 1
            elif 2 in coin_cost_array:
                prior_set = coin_cost_array.index(2)
                coin -= 2
                
            if coin < 0:
                return round_num
            if prior_set != -1:
                for x in able_friends[prior_set]:
                    cur_card[x] = 0
            if round_num == (max_round_num-1):
                print(f'끝까지왔네!!!')
                return max_round_num
            continue
        else:
            print(f'가능한 조합이 없네!!!')
            return round_num
    