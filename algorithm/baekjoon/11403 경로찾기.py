"""
11403 경로찾기

정말 간단했다. 입력받은 행렬을 그래프로 변환해주고 변환한 그래프를 bfs를 통해 탐색하면 된다. 해당 시작점에서 방문 가능한 지점들을 visited배열에 저장하고 
visited배열을 이용하여 행렬을 채워준다.

"""

from collections import deque

N = int(input())

graph = []


for i in range(N+1):
    graph.append([])

# 그래프 생성
for i in range(1,N+1):
    data = list(map(int,input().split()))
    for j in range(len(data)):
        if i-1 != j:
            if data[j] == 1:
                graph[i].append(j+1)

grid = [['0'] * N for _ in range(N)]

# 시작 위치를 받는다
def bfs(start):
    q = deque()
    q.append(start)
    while q:
        now_start = q.popleft()
        for n in graph[now_start]:
            if n not in visited:
                visited.add(n)
                q.append(n)


for i in range(1,N+1):
    visited = set()
    # 시작위치는 i
    bfs(i)
    if not visited:
        continue
    else:
        for j in visited:
            grid[i-1][j-1] = '1'

for i in grid:
    print(" ".join(i))