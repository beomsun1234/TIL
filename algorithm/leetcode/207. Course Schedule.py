class Solution:
    """
    207. Course Schedule
    Input  : numCourses = int, prerequisites[i] = [ai,bi] -> a과목을 수강하기위해 b과목을 들어야한다 int 2d 배열
    Output : bool -> 수강할 수 있으면 True 없으면 False
    
    Constraints
    
    1 <= numCourses <= 105
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.
    
    DS - DFS
    
    1. numCourses 크기의 visited라는  배열을 선언 후  False로 초기화 -> visited = [False]* numCourses, 방문 표시 이미 방문했음 다시 방문하지 않기 위해 
    2. numCourses 크기의 taken이라는 배열 선언 -> dfs 완료 후 확인한 수강 과목을 체크 하기 위해 선언
    3. prerequisites을 그래프로 변형
    4. 0번 부터 dfs를 시작한다.
    5. if 0번 코스를 방문했는데 다시 0번 코스를 방문한다면 사이클 발생 -> 사이클이 발생했다는건 해당 과목을 이수할 수 없다.
    6. dfs가 완료되면 해당 코스를 다시 방문 안하기 위해 taken 배열의 해당 코스 인덱스를 True로 변경 
    7. taken[now]이미 확인 완료한 코스를 확인 할 경우 return true 
    
    time - O(v+e)
    v=정점
    e=간선
    
    회고
    
    첫번째 제출에서 시간 초과가 나왔다 input = 100일 때
    
    def dfs(start):
            if visted[start]:
                return False
            visited[start] = True
            for nextStart in graph[start]:
                if not dfs(nextStart):
                    return False
            visited[start] = False 
            return True 
    
    visited가 초기화 되면서 계속 돌기 때문이다 이럴 경우 모든 정점과 간선을 방문하고 사이클을 찾기 위해 모든 정점에 대해서 DFS를 수행하여 O(v(v+e))되서 시간 초과가 나온다... 모든 정점에 대해 사이클을 찾지 않고 하번의 dfs로 사이클을 찾는 방법을 몰랐다..
    출저 : https://hongl.tistory.com/60?category=922907 여기 잘 설명해주신 분이 있어서 정말 감사하다. dfs를 수행하다 재귀 탐색이 종료 되지 않았는데 다시 방문하게 된다면 사이클이 있다고 판단할 수 있다. 즉 사이클이 존재하는 노드와 연결된 노드로 부터 사이클 존재여부를 바로 확인 할 수 있다
    나는 taken 배열을 통해 해당 정점이 dfs가 종료됐는지 확인하고 종료됐으면 해당 정점을 탐색하지 않는다. 
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        ret = True
        graph = []
        visited = [False]*numCourses
        taken = [False]*numCourses
        for i in range(numCourses):
            graph.append([])

        for i, j in prerequisites:
            graph[i].append(j)
        def dfs(start,visited,taken):
            if taken[start]:
                return True
            if visited[start]: ## 방문한곳 다시 방문하면 사이클
                print("1")
                return False
            visited[start] = True  # 방문
            for nextStart in graph[start]:
                if not dfs(nextStart,visited,taken):
                    return False
            taken[start] = True # 최종완료
            return True

        for i in range(numCourses):
            if not visited[i]: 
                if not dfs(i,visited,taken):
                    return False
            
        return ret
        
        