"""
dfs와 bfs 1260

정말 간단했다. 생각해줘야 할 부분은 각 정점에 해당하는 간선들을 정렬해줘야한다는것 말고는 딱히 생각 할 게 없는 문제 같다.



"""
from collections import deque

v, e , start = map(int,input().split())

graph = []

## 그래프 생성
for i in range(v+1):
    graph.append([])

for i in range(e):
    vv,ee = map(int,input().split())
    graph[vv].append(ee)
    graph[ee].append(vv)

## 그래프의 각 정점에대해서 간선 정렬
for idx, eee in enumerate(graph):
    if eee:
        eee.sort()
        graph[idx] = eee
ret = []
visited = [False] * (v+1)
ret.append(start)
visited[start] = True
# dfs탐색
def dfs(vv,depth):
    for e in graph[vv]:
        if not visited[e]:
            visited[e] = True
            ret.append(e)
            dfs(e,depth+1)

# bfs탐색
def bfs():
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        for e in graph[node]:
            if not visited[e]:
                visited[e] = True
                ret.append(e)
                q.append(e)
        
dfs(start,0)
print(' '.join(map(str,ret)))
## dfs 종료 후 초기화
ret = []
visited = [False] * (v+1)
ret.append(start)
visited[start] = True
bfs()
print(' '.join(map(str,ret)))
