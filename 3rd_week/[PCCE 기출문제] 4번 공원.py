#https://school.programmers.co.kr/learn/courses/30/lessons/250121

"""
## 알아야할 함수 ##
- list.sort(reverse=True) or .reverse()
- string이 요소인 리스트에서 max 사용하면 알파벳순이 숫자보다 우선순위

## 특이사항 ##
점수 : /100
- 범위를 설정할때는 의도에 맞게 설정됐는지 print해보면서 꼭 확인해보기! edge case에 걸릴 수 있음
##################
"""


def solution(mats, park):
    answer = -1
    row = len(park)
    col = len(park[0])
    # 큰 순으로 정렬
    mats.sort(reverse=True)
    for mat in mats:
        if row>=mat and col>=mat:
            for i in range(row-mat+1):
                for j in range(col-mat+1):
                    #돗자리 있는 칸은 패스
                    if park[i][j] != "-1":
                        continue
                    #돗자리 없는 칸은 돗자리 길이를 더한만큼의 범위의 리스트 생성
                    else:
                        mats_list = []
                        for m in range(mat):
                            for n in range(mat):
                                mats_list.append(park[i+m][j+n])
                        # print(f'---------------------')
                        # print(f'돗자리 : {mat}')
                        # print(f'[i][j] : {i},{j}')
                        # print(f'mats_list : {mats_list}')
                        # print(f'max(mats_list) : {max(mats_list)}')
                    #리스트 값 중에 -1이 max값이면 해당 돗자리 return
                        if max(mats_list) == "-1":
                            return mat
    return answer