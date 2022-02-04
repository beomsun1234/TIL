"""
1753 - 최단경로
"""
import sys
import heapq
INF = 100000000
input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
graph = []
for i in range(V+1):
    graph.append([])

#방향그래프 설정
for i in range(E):
    v,e,c = map(int,input().split())
    graph[v].append((e,c))

visited = [INF] * (V+1)

q = []

heapq.heappush(q, (0,start))
visited[start] = 0
while q:
    cost , node = heapq.heappop(q)
    for e in graph[node]:
        # 0->도시, 1-> 비용
        next_cost = e[1] + cost
        if visited[e[0]]>next_cost:
            visited[e[0]]=next_cost
            heapq.heappush(q,(next_cost,e[0]))

for idx in range(1,V+1):
    if visited[idx] != INF:
        print(visited[idx])
    else:
        print("INF")
