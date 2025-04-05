# https://school.programmers.co.kr/learn/courses/30/lessons/258711

"""
## 알아야할 함수 ##
1. from collections import deque : pop, popleft를 사용하기 위함 deque([])와 같이 선언

## 특이사항 ##
점수 : /100

##################
"""

from collections import deque

def bfs(g,start,visited):
	queue = deque([start])
	visited[start] = True
    
	while queue:
		v = queue.popleft()
		print(v,end=' ')
		for i in g[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

g =[
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7],
]

print(g[1])
visited = [False] * 9

bfs(g,1,visited)