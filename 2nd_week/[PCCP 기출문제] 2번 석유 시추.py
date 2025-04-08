# https://school.programmers.co.kr/learn/courses/30/lessons/250136

"""
## 알아야할 함수 ##
- sorted() : 리스트를 정렬해줌
- list(set())은 요소들이 list일 경우 작동하지 않음. 일일이 tuple
- list.append() 그리고 set.add()
- result = [a * b for a, b in zip(list1, list2)] 리스트 요소들끼리 곱해주려면 이렇게 해야함
- 리스트들끼리는 비교할 수 없으니, 비교하려면 tuple을 사용해야함 (hashable!!!)
- set.update() 그리고 list.extend()
- lambda : 한번만 쓸 간단한 함수 정의 문법 : [lambda 매개변수: 리턴값]
- node = next(iter(oil_nodes)) -> for문으로 하나씩 꺼내는게 아니라 while문을 사용할때 다음 node를 꺼내는 작업!!!

## 특이사항 ##
점수 : 86.7/100
(시간 초과)
##################
"""

def dfs(start_node, oil_nodes, sizeofland):
    oil_group = [start_node]
    visited = {start_node}
    n, m = sizeofland
    # 오일이 있는 노드들의 리스트에 대해서 dfs 진행
    while oil_group:
        cur_node = oil_group.pop()
        a, b = cur_node
    #시작 노드로부터 전후좌우 더해가면서 dfs
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = a + dx, b + dy
            neighbor = (nx, ny)
            if 0 <= nx < n and 0 <= ny < m:
                if neighbor in oil_nodes and neighbor not in visited:
                    oil_group.append(neighbor)
                    visited.add(neighbor)
    return visited

def solution(land):
    sizeofland = (len(land), len(land[0]))
    n, m = sizeofland
    # oil이 있는 node들만 set에 저장
    oil_nodes = {(i, j) for i in range(n) for j in range(m) if land[i][j] == 1}
    
    # oil 덩이들 연결 짓기
    column_score = [0] * m
    while oil_nodes:
        node = next(iter(oil_nodes))
        group = dfs(node, oil_nodes, sizeofland)
        oil_nodes-=group
            
        # 덩이당 석유량
        oil_amount = len(group)

        # 각 석유덩이들이 존재하는 열
        involved_columns = set(y for _, y in group)
        # 존재하는 열에 석유량 더해줘서 누적시키기
        for col in involved_columns:
            column_score[col] += oil_amount
        # 누적된 석유량 중 최댓값 산출하기
    return max(column_score) if column_score else 0
        