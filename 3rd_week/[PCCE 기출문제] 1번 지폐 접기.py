#https://school.programmers.co.kr/learn/courses/30/lessons/340199

"""
## 알아야할 함수 ##
- 반올림 : round() | 올림 : math.ceil() | 내림 : math.floor() | 버림 : math.trunc()

## 특이사항 ##
점수 : 100/100
왜 답 다 알려줌?
ez
##################
"""

def solution(wallet, bill):
    answer = 0
    while min(bill) > min(wallet) or max(bill) > max(wallet):
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2
        answer += 1
            
    return answer