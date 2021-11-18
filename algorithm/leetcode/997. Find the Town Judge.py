class Solution:
    
    """
    997. Find the Town Judge.md
    Input  : n =  사람 수(라벨링) int, trust 2차원 정수 배열,
    Output : int -> 1~n 중에 1,2,3, 조건을 만족하는 번호
    
    Constraints:
    1 <= n <= 1000
    0 <= trust.length <= 104
    trust[i].length == 2
    All the pairs of trust are unique.
    ai != bi
    1 <= ai, bi <= n
    
    DS - dfs, 그래프
    
    쉬운 방법도 있으나 dfs와 그래프를 학습하기위해 dfs와 그래프를 사용해 보았다.
    
    1. 주어진 trust 배열을 그래프로 변경한다.
    1.1 trustNum이라는 변수를 선언해서 후보자를 믿는 사람의 수를 카운트 해준다.
    2. visited 배열을 만들어 준다.
    3. 주어진 그래프에서 간선이 하나도 없을 경우 이친구는 유력한 town judge이기에 후보자 변수를 두어 저장해둔다.
    4. 후보자를 제외하고 모든 그래프를 dfs로 탐색하고 방문하면 visited 배열을 true로 변경해준다.
    5. 만약 방문한 곳이 후보자이면 trustNum의 카운트를 증가시켜준다.
    6. 만약 trustNumd이 후보자를 제외한 숫자인 n-1일 경우 이친구는 town judge가 된다.
    
    time = o(v+e)
    """
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = []
        visited = [False]*(n+1)
        global trustNum
        trustNum = 0
        candidateTJ = 0
        
        for i in range(0,n+1):
            graph.append([])
        for p,tp in trust:
            graph[p].append(tp)
        
        for v,e in enumerate(graph):
            if v!=0 and e==[]:
                candidateTJ = v
                
        if candidateTJ == 0:
            return -1
        
        def dfs(graph,v,visited, candidateTJ):
            global trustNum
            if v == candidateTJ:
                trustNum += 1
                return 
            if visited[v]:
                return 
            visited[v] = True
            for nv in graph[v]:
                dfs(graph,nv,visited,candidateTJ)
                

        for v in range(1,n+1):
            if v!=candidateTJ:
                if not visited[v]:
                    dfs(graph,v,visited,candidateTJ)

        print(trustNum)
        if n-1 == trustNum:
            return candidateTJ
        
        return -1