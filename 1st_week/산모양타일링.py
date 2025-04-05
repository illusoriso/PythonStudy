# https://school.programmers.co.kr/learn/courses/30/lessons/258705

"""
## 알아야할 함수 ##

## 특이사항 ##
점수 : 100/100
##################
"""

def solution(n, tops):

    MODULAR_NUMBER = 10007

    # 공유 삼각형을 포함해서 경우의 수를 계산하는 DP (DP_SHARE)
    DP_SHARE = [0] * n

    # 공유 삼각형을 포함하지 않고 산출되는 경우의 수를 계산하는 DP (DP_ONLY)
    DP_ONLY = [0] * n

    # 최초의 경우의 수를 산정
    if tops[0] == 1: # 탑이 존재하는 경우
        DP_SHARE[0] = 4 # 우측하단을 포함한 경우의 수를 산정하면 4개의 경우
        DP_ONLY[0] = 3  # 우측하단을 제외하고 경우의 수를 산정하면 3개의 경우
    else: # 탑이 없는 경우
        DP_SHARE[0] = 3 # 우측하단을 포함한 경우의 수를 산정하면 3개의 경우
        DP_ONLY[0] = 2  # 우측하단을 제외하고 경우의 수를 산정하면 2개의 경우

    # 순회하면서, DP연산 진행
    for i in range(1, n):
        top = tops[i]

        if top == 1: # 탑이 있는 경우
            DP_SHARE[i] = (DP_SHARE[i-1] * 3 + DP_ONLY[i-1]) % MODULAR_NUMBER
            DP_ONLY[i] = (DP_SHARE[i-1] * 2 + DP_ONLY[i-1]) % MODULAR_NUMBER
        else:  # 탑이 없는 경우
            DP_SHARE[i] = (DP_SHARE[i-1] * 2 + DP_ONLY[i-1]) % MODULAR_NUMBER
            DP_ONLY[i] = (DP_SHARE[i-1] + DP_ONLY[i-1]) % MODULAR_NUMBER

    # 답은 모든 경우를 포함한 공유 삼각형을 포함한 경우의 수를 반환해야함!
    return DP_SHARE[-1]