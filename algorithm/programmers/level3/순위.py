"""
level 3 순위
Input = n -> 권투선수의 수(1~n 라벨링), results -> 경기결과[[4,3]] -> 4번선수는 3번을 이김
Output = 결과과 확실한 선수 번호 return ->int

constraints
-선수의 수는 1명 이상 100명 이하입니다.
-경기 결과는 1개 이상 4,500개 이하입니다.
-results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
-모든 경기 결과에는 모순이 없습니다.

DS - 그래프, DFS

1. 내가 이긴 사람(1이 2를 이겼고 2가 3을 이겼으면 1은 3과 붙어보지 않아도 3을 이긴다)의 그래프를 만든다.
2. 내가 진 사람(반대 3은 2에게 졌고 2는 1에게 졌으므로 3은 1과 붙어보지 않아도 1에게 진다)의 그래프를 만든다.
3. 이긴 사람을 방문체크 할 visitedWin을 만든다
4. 진 사람을 방문 체크 할 visitedLose을 만든다.
5. 이긴사람을 탐색한다. cnt라는 변수를 선언해서 이긴 사람의 카운트를 체크 한다.
6. 탐색이 종료되면 방문표시를 초기화하고 cnt변수를 해당 선수 번호에 저장한다.
7. 진 사람을 탐색한다. cnt라는 변수를 선언해서 진 사람의 카운트를 체크 한다.
8.탐색이 종료되면 방문표시를 초기화하고 cnt변수를 해당 선수 번호에 저장한다.
9. 각 선수 마다 이긴 사람과 진사람의 수를 더한 값이 n-1(전체 선수에서 자기 자신을 뺀 값)이 같다면 순위를 정확히 매길 수 있는 선수이다. 해당 조건을 만족할 때 마다 answer +1 해준다

time = o(v)

# 처음에 쉽다고 생각해서 무작정 풀었는데 2개의 케이스만 맏고 전부 틀렸다....
dfs로 각 선수를 방문하고 카운트를 해준 후 해당 선수의 카운트가 n-1이면 해당 선수의 번호를 리턴해줬다.. 문제 자체를 잘 못 이해한거다.... 나는 정확하게 순위를 매길 수 있는 사람의 번호 중 가장 먼저 찾은 사람 1명만을 리턴했다.. 계속 틀려서 힌트를 보니 선수의 번호를 리턴하는게 아닌 몇명이나 정확하게 순위를 매길 수 있는지를 물어보는거다....   
"""
def solution(n, results):
    answer = 0
    visitedWin = [False]*(n+1)
    visitedLose = [False]*(n+1)
    winGraph = []
    loseGraph = []
    global cnt
    cnt = 0
    winCnt = [0]*(n+1)
    loseCnt = [0]*(n+1)
    for v in range(0,n+1):
        winGraph.append([])
        loseGraph.append([])
    for v, e in results:
        winGraph[v].append(e)
        loseGraph[e].append(v)
        
    print(winGraph)
    print(loseGraph)
    def dfs(graph,v,visited):
        global cnt     
        visited[v] = True
        for e in graph[v]:
            if not visited[e]:
                cnt+=1
                dfs(graph,e,visited)
    
    for v in range(1,n+1):
        # 다시 방문 할 수 있도록 초기화
        visitedWin = [False]*(n+1)
        cnt = 0
        dfs(winGraph,v,visitedWin)
        winCnt[v] = cnt
        # 다시 방문 할 수 있도록 초기화
        visitedLose= [False]*(n+1)
        cnt = 0
        dfs(loseGraph,v,visitedLose)
        loseCnt[v] = cnt
    print(winCnt,loseCnt)
    
    for v in range(1,n+1):
        if winCnt[v] + loseCnt[v] == n-1:
            answer +=1
    
    return answer