class Solution:
    """
    1319. Number of Operations to Make Network Connected
    Input = n (computers), 2차원 배열 connections (연결 정보) [[a,b]] -> a와 b가 연결됨
    Ouput = int (최소 횟 수 모든 컴퓨터를 연결 시키기 위한)
    
    Constraints
    - 1 <= n <= 10^5
    - 1 <= connections.length <= min(n*(n-1)/2, 10^5)
    - connections[i].length == 2
    - 0 <= connections[i][0], connections[i][1] < n
    - connections[i][0] != connections[i][1]
    - There are no repeated connections.
    - No two computers are connected by more than one cable.
    
    DS - DFS, 그래프
    
    1. visited 배열을 선언해서 방문했던 곳은 다시 방문 하지 않도록 선언 해준다.
    2. 주어진 connections배열의 연결 정보를 바탕으로 그래프를 만든다.(양방향)
    2-1. 주어진 connections배열의 길이가 즉 연결 정보가 컴퓨터의 수보다 작을 경우 저누 연결 할 수 없으므로 -1을 리턴(edge case)
    
    3. 문제를 보면 모든 컴퓨터를 연결하기 위한 최소한 횟수를 리턴하는 것이다. 주어진 테스트 케이스 1번을 예로 들면 0,1,2는 그룹 1이라고 가정하면 남아있는 3은 그룹 2가 된다. 그룹 1과 2를 연결하기 위해서는 1개의 선이 필요로 한다. 즉 시작 점에 있는 2개의 그룹을 연결하기 위해선 n-1인 1개가 필요하다. 3개의 그룹을 연결하기 위해선 2개가 필요할 것이다.
    4. dfs로 그룹이 몇개 인지 찾는다.
    5. 찾은 후 그룹의 갯수에서 -1한 값이 최소 횟수가 된다.
    
    0번 컴퓨터부터 탐색을 진행하고 방문했던 곳을 방문 할 경우 탐색을 하지 않는다.
    
    
    time = O(v+e)
    space = O(v+e)
    """
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = []
        
        
        if n-1 > len(connections):
            print('There are not enough cables')
            return -1
        
        for v in range(0,n):
            graph.append([])
            
        for v,e in connections:
            graph[v].append(e)
            graph[e].append(v)
        
        print(graph)
        
        visited = [False] * n
      
        def dfs(v,graph,visited):
            if visited[v]:
                return 
            visited[v] = True
            for e in graph[v]:
                dfs(e,graph,visited)
    
        ret = 0
        for i in range(0,n):
            if not visited[i]:
                print(i)
                dfs(i,graph,visited)
                ret+=1
    
        return ret-1



