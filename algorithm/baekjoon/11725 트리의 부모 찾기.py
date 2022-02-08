"""
11725 트리의 부모 찾기
"""

from collections import deque

N = int(input())
graph = []

for i in range(N+1):
    graph.append([])

for i in range(N-1):
    data = list(map(int, input().split()))
    graph[data[0]].append(data[1])
    graph[data[1]].append(data[0])

parent = [0] * (N+1)

q  = deque()
q.append(1)
parent[1] = 1
while q:
    node = q.popleft()
    for i in graph[node]:
        if parent[i] ==0:
            parent[i] = node
            q.append(i)

for i in range(2,N+1):
    print(parent[i])