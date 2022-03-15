"""
1238 파티

간단했다. 처음 제출했을때 테스트케이스는 통과하나 9%에서 틀렸다고 나왔다... 문제를 다시 읽어보니 오고가는 값의 최대값을 구하는 것 이다.... 근데 나는 다시 돌아오는 거리를 계산해 주지 않았다...
다시 돌아오는 것 까지 추가해주니 성공 할 수 있었다. 다익스트라를 통해 최단거리를 구현한 후 각 시작 마을에서 X까지의 거리를 구하고 X에서 i까지 돌아가는 거리를 구한 후 더해서 그 값이 최대인 것을 구하면 된다.

"""
INF = int(1e9)
import heapq
# 단반향이다 다시 돌아오지 못한다. 거쳐서 돌아와야함
N, M ,X = map(int,input().split())
graph = []
for i in range(N+1):
    graph.append([])
for i in range(M):
    v,e,c = map(int,input().split())
    graph[v].append((e,c))
# 최단거리 구하기
def dijkstra(start_node):
    q = []
    visited = [INF] * (N+1)
    heapq.heappush(q,(0,start_node))
    visited[start_node] = 0 
    while q:
        cost, node = heapq.heappop(q)
        for e in graph[node]:
            next_cost = e[1] + cost
            #다음 가려는 곳의 비용이 이전 비용과 비교해서 작을 경우 갱신
            if visited[e[0]] > next_cost:
                visited[e[0]] = next_cost
                heapq.heappush(q,(next_cost,e[0]))
    return visited
answer = 0
for i in range(1,N+1):
    go = dijkstra(i)
    back_home = dijkstra(X)
    # x까지가는데 거리 + X에서 다시 집으로 돌아오는데 거리
    answer = max(answer, go[X] + back_home[i])
print(answer)
