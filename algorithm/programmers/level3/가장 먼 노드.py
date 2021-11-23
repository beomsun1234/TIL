"""
level 3 가장 먼 노드

Input = 간선에 대한 정보가 담긴 2차원 배열 vertex, 
Output = 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return

Constraints
- 노드의 개수 n은 2 이상 20,000 이하입니다.
- 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
- vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.

DS - BFS, 그래프

1. 주어진 vertex를 바탕으로 그래프를 만든다.
2. visited배열을 선언해서 방문했던곳 다시 방문하지 않도록 설정
3. dist 배열을 선언해서 하나의 간선을 지날때 마다 dist배열을 카운트해준다. (거리 증가)
4. dist라는 배열의 값이 0일 경우만 카운트해준다.(거리체크)
5. 이후 다음 정점으로 bfs를 수행한다.
6. bfs가 끝나면 dist배열에 값을 확인하여 큰값이 몇개가 있는지 체크하고 return하면 된다.

# 처음에 dfs로 접근했다가 너무 코드가 복잡해졌다.. 아직 재귀를 잘 다루지 못하는 것 같다. 재귀가 아닌 bfs로 접근하니 쉽게 풀 수 있었다.

"""
from collections import deque
def solution(n, edge):
    answer = 0
    visited = [False]*(n+1)
    dist = [0] * (n+1)
    ck = [0] *(n+1)
    graph = []
    for i in range(0,n+1):
        graph.append([])
    for v,v2 in edge:
        graph[v].append(v2)
        graph[v2].append(v)
        
    def bfs(v, visited, graph):
        q = deque()
        q.append((v,0))
        while q:
            vertex,c = q.popleft()
            if not visited[vertex]:
                visited[vertex]= True
                if dist[vertex] == 0:
                    dist[vertex] = c
                for e in graph[vertex]:
                    q.append((e,c+1))
    bfs(1, visited, graph)
    print(dist)
    for v in dist:
        if v == max(dist):
            answer+=1
    
    return answer
    
