"""
level-2 Summer/Winter Coding(~2018) - 배달

처음에 쉽게 bfs를 이용해서 최단거리를 갱신해나갔다.. 처음로직은 거리를 즉 방문 지점을 모두 0으로 초기화 해주었는데 그럴 경우 그것이 최단거리가 되므로 0으로 초기화 하기보다 무한대로 초기화 해야했다.. 
bfs를 사용해서 최단거리르 갱신해주면서 주어진 해당 거리가 주어진 k보다 작으면 배달가능하며 answer+1을 하는 식으로 접근했다.

"""
from collections import deque
def solution(N, road, K):
    answer = 0

    graph = []
    
    ## 그래프 생성
    for i in range(0, N+1):
        graph.append([])
    
    for v,e,c in road:
        graph[v].append((e,c))
        graph[e].append((v,c))
    ## bfs
    visited = [float('inf')] * (N+1) # 방문 거리 무한대로 초기화
    q = deque()
    q.append((1,0)) # 시작은 1이고 해당 코스트는 0이다
    visited[1] = 0 # 1번째가 시작으므로 해당 위치를 0으로 초기화
    while q:
        node, nodeCost = q.popleft() #큐에서 노드랑 코스트를 꺼낸다
        for e,eCost in graph[node]: # 해당 노드의 엣지를 찾는다
            if visited[e] > nodeCost + eCost: #찾은 엣지의 거리 값이 현재 노드의 거리와 찾은노드의 거리를 더한값보다 크면 해당 
                visited[e] = nodeCost+eCost # 엣지의 거리 값을 갱신
                q.append((e,nodeCost+eCost)) # 큐에 찾은 엣지와 갱신된 코스트를 추가
    
    ## 방문한 거리가 k보다 작거나 같은 개수 찾기
    for i in range(2,N+1):
        if visited[i] <=K:
            answer+=1
    return answer+1
