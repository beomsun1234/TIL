"""
2021 KAKAO BLIND RECRUITMENT - 합승 택시 요금

"""
import heapq
def dj(start_node,visited,graph,n,a,b):
    visited = [100000001 ] * (n+1)
    route = []
    heapq.heappush(route, (0,start_node))
    while route:
        cost, node = heapq.heappop(route)
        for e_node, e_cost in graph[node]:
            next_cost = e_cost + cost
            if next_cost < visited[e_node]:
                visited[e_node] = next_cost
                heapq.heappush(route,(next_cost,e_node))

    return visited[a], visited[b] , visited

def solution(n, s, a, b, fares):
    # (start_node,visited,graph,n)
    graph = []
    for _ in range(n+1):
        graph.append([])
    for c,d,f in fares:
        graph[c].append((d,f))
        graph[d].append((c,f))
    visited = [1000000] * (n+1)
    ca,cb, tmp_visited = dj(s,visited,graph,n,a,b)
    answer = ca + cb
    for i in range(1,n+1):
        dist = tmp_visited[i]
        if s == i:
            continue
        c_a, c_b, tmp = dj(i,visited,graph,n,a,b)
        if i == a:
            c_a = 0
        if i == b:
            c_b = 0
        dist = dist + c_a + c_b
        answer = min(answer, dist)
    return answer