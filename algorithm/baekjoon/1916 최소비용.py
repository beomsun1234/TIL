"""
다익스트라 - 최소비용 - 1916

처음 풀이는 bfs로 최단거리를 계산하여 해당 목적지에 최종 거리를 계산해주는 방법으로 접근했다.. 결과는 메모리 초과가 나왔고 아마 시간 초과도 날 것이다.. 이

다익스트라로 접근하기로 마음 먹었고 해당 다익스트라 알고리즘의 최적방법??인 힙 큐를 이용해서 접근했다. 여기서 주의할 점이 거리를 힙 큐 첫번째에 넣어 주어야하고

여기서 if 현재노드 == 목적지 이면 종료 시켜주는 로직을 추가하지 않으면 시간 초과의 지옥에 빠질것이다... 

from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

nosun = []

for i in range(N+1):
    nosun.append([])

for i in range(M):
    city_no1, city_no2, cost = map(int, input().split())
    nosun[city_no1].append((city_no2,cost))

start_city , des_city = map(int, input().split())

visited = [float("inf")] * (N+1)
q = deque()
q.append((start_city, 0))
visited[start_city] = 0
while q:
    node, cost = q.popleft()
    for e in nosun[node]:
        if visited[e[0]] > cost:
            visited[e[0]] = cost+e[1]
            q.append((e[0], cost+e[1]))

print(visited[des_city])
-- 메모리 초과

"""
import heapq
import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
INF = 987654321
nosun = []

for i in range(N+1):
    nosun.append([])

for i in range(M):
    city_no1, city_no2, cost = map(int, sys.stdin.readline().split())
    nosun[city_no1].append((city_no2,cost))

start_city , des_city = map(int, sys.stdin.readline().split())
visited = [INF] * (N+1)

def dijkstra():
    q = []
    heapq.heappush(q, (0, start_city))
    visited[start_city] = 0
    while q:
        cost , node  = heapq.heappop(q)
        if node == des_city:
            break
        for e in nosun[node]:
            next_cost = cost+e[1]
            if next_cost < visited[e[0]] :
                visited[e[0]] = next_cost
                heapq.heappush(q, (next_cost, e[0]))

dijkstra()

print(visited[des_city])