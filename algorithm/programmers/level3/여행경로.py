"""

Input = 2차원 배열 tickets
Ouput = 1차원 배열 공항 경로

Constraints 
-  항상 "ICN" 공항에서 출발합니다.
- 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
- 주어진 공항 수는 3개 이상 10,000개 이하입니다.
- tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
- 주어진 항공권은 모두 사용해야 합니다.
- 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
- 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다

DS - DFS, 그래프

1. 주어진 티켓 정보를 그래프로 변환한다(딕셔너리로(key,value)),
2. 그래프에서 목적지를 ([a,b]이면 b가 목적지다) 알파벳 순으로 정렬한다.
3. 항상 ICN에서 출발하기에 dfs 시작 위치를 ICN으로 설정하고 dfs를 수행한다.
4. while문을 돌면서 현재 공항에서 다음 공항으로 갈수 있는 경우가 2가지 이상인 경우 알파벳이 빠른 곳을 먼저 방문하고 스택에서 방문한 곳은 그래프에서 제거해준다.
5. dfs가 끝나면 모두 다 방문했으 그래프에는 시작점만 남을 것이고 역순으로 값이 저장되어 있을 것이다. 이것을 다시 reverse를 통해 리버스 해준면 값이 된다.

time = O(v+e)
space = O(v+e)
# 회고
문제를 잘 못 파악했던 것 같다.. 예를 들면"ICN" - "ATL" - "ICN" - "SFO" - "ATL" - "SFO" 같이 같은 곳을 다시 방문 할 수 있다는 것이다.. dfs 종료 조건을 여러 생각해 봤지만 잘 떠오르지 않았다.. 첫번째로 시도한게 depth를 줘서 주어진 티켓의 길이랑 같아지면 종료 시키는 방법을 해보았지만 테스트케이스 1,2를 통과하지 못했다...  
힌트를 보고 풀 수 있었다..
"""
from collections import defaultdict
def solution(tickets):
    answer = []
    ret = []
    graph = defaultdict(list)
    for f, t in tickets:
        graph[f].append(t)
    for v in graph:
        graph[v].sort()
    
    def dfs(graph, start,ret,depth):
        while graph[start]:
            print(start)
            dfs(graph,graph[start].pop(0), ret,depth+1)
        answer.append(start)
        
    dfs(graph,'ICN',ret,0)
    answer.reverse()
    
    return answer