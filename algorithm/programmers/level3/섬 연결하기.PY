"""
level3 - 그리디, 섬 연결하기
처음 시도는 bfs를 이용해서 내가 이동했을때 최소값을 갱신해 주는 방법으로 했다... 주어진 테케는 통과하지만 제출할 경우 통과 할 수 없다.. 원인을 파악하지 못했지만 잘못된 접근 이었던 것 같다. 사이클이 형성 될 경우도 고려하지 않았다.. 아래는 처음 작성한 코드이다.
bfs
from collections import deque
def solution(n, costs):
    answer = 0
    graph = []
    for i in range(n):
        graph.append([])
    for i,j,cost in costs:
        graph[i].append([j,cost])
        
    visited = [1200] * (n)
    # 0 -> node, 1->cost
  
    print(graph)
    q = deque()
    q.append((0, 0))
    visited[0] = 0
    while q:
        node,cost = q.popleft()
        for e,c in graph[node]:
            if  visited[e] > c:
                visited[e] = c
                q.append((e,c))
    print(visited)
    return sum(visited)

두번째 생각한 방식은 최소신장트리를 생각했다.. 생각만 했지 구현 방법을 몰라서 크루스칼 알고리즘을
찾아보며 문제에 대입하니 성공했다.. 어떻게 보면 정말 간다하지만 어떤 알고리즘을 적용하느냐에 따라 갈리는 것 같다..
"""
## 내 풀이

# 부모찾기
def find(parent,x):
    if parent[x] == x:
        print(x)
        return x
    parent[x] = find(parent,parent[x])
    return parent[x]
# 두 원소가 속한 집합을 합치기 (간선 연결한다고 생각!)
def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

    
def solution(n, costs):
    parent = [0] * n
    # 부모테이블 초기화
    for i in range(0,n):
        parent[i] = i
    graph = []
    answer = 0
    for i,j,cost in costs:
        graph.append((cost,i,j))
    graph.sort()
    for e in graph:
        cost,a,b = e
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += cost
    
    return answer
    

