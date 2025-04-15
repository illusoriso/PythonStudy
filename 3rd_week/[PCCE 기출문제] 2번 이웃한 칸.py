#https://school.programmers.co.kr/learn/courses/30/lessons/250125

"""
## 알아야할 함수 ##
- 

## 특이사항 ##
점수 : 100/100
예외처리하는 것이 중요!!
ez
##################
"""

def solution(board, h, w):
    answer = 0
    near_list = [[1,0],[-1,0],[0,1],[0,-1]]
    ego = board[h][w]
    for near in near_list:
        if near[0]+h >= len(board) or near[0]+h < 0 or near[1]+w >= len(board[0]) or near[1]+w < 0:
            continue
        if board[near[0]+h][near[1]+w] == ego:
            answer+=1
        
    return answer