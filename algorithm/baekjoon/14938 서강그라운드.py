"""
14938 서강그라운드 
18:00 ~ 18:30

지금 생각하는 접근 방식은 예은이가 낙하한 지역을 기준으로 방문 할 수 있는 지역의 최단거리를 구하고 구한 거리를 이용하여 예은이가
낙하한 지점에서 해당 지역을 방뭉하는데 걸리는 거리가 수색범위 안에 있다면 해당 아이템을  얻을 수 있다. 각 낙하지점에 따라 얻을 수 있는 최대 아이템수를 리턴

해당 방법으로 접근해서 정답을 도출할 수 있었다. 1~N+1 까지의 낙하지점에 따라 최단거리를 구해주고 구한 최단거리를 이용해서 낙하지점에 따라 얻을 수 있는 아이템의 개수의 최대값을 구한다.

"""
import heapq


# 지역의 개수 n, 예은이의 수색범위 m , 길의 개수 r 
N, M , R = map(int,input().split())

graph = []

for i in range(N+1):
    graph.append([])

## 각 지역의 아이템 수
items = list(map(int,input().split()))

# 지역의 번호 a, b, 그리고 길의 길이 l 
for i in range(R):
    a,b,l = map(int,input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))

# 최단거리 구하기
def dj(start):
    visited[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, node = heapq.heappop(q)
        for e in graph[node]:
            # e idx 0번째 - node, 1 - dist
            next_dist = e[1]+ dist
            if visited[e[0]]>next_dist:
                visited[e[0]] = next_dist
                heapq.heappush(q,(next_dist, e[0]))

answer = 0

for i in range(1,N+1):
    visited = [float('inf')] * (N+1)
    dj(i)
    item_cnt = 0

    # 낙하지점을 기준으로 최단거리를 확인하여 얻을수 있는 아이템의 개수를 확인한다.
    for idx,dist in enumerate(visited):
        if dist <= M:
            item_cnt += items[idx-1]
    answer = max(answer, item_cnt)

print(answer)