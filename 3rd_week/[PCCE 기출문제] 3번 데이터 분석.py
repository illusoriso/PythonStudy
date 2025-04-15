#https://school.programmers.co.kr/learn/courses/30/lessons/250121

"""
## 알아야할 함수 ##
- from operator import itemgetter
- answer = sorted(data, key=itemgetter(val_ext_idx))
- itemgetter(val_ext_idx): data 리스트의 각 요소에서 val_ext_idx번째 값을 꺼내주는 함수 역할을 함.

## 특이사항 ##
점수 : /100
for문을 돌릴때 탐색하는 리스트의 값/길이가 반복문 중에 변화한다면 항상 조심할 것!
##################
"""

from operator import itemgetter

def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    name_list = ["code", "date", "maximum", "remain"]
    ext_idx = name_list.index(ext)
    filtered_data = []
    #기준보다 작은 값만 고르기
    for idx, dat in enumerate(data):
        if dat[ext_idx] < val_ext:
            filtered_data.append(dat)
    #골라진 값들 중 기준에 따라서 오름차순으로 정리
    sort_by_idx = name_list.index(sort_by)
    answer = sorted(filtered_data, key = itemgetter(sort_by_idx))
    return answer