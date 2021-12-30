"""
LEVEL 2 - 땅따먹기

dfs로 접근했더니 시간 초과가 발생했다.. 당연...  행의 개수 N : 100,000 이하의 자연수이기에 내 코드의 시간복잡도는 O(2^N)이다.. 그리디를 사용하는 문제인것같다..
아래는 DFS를 사용하여 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 모든 경우의 수를 찾았다.. 

이전 행의 최대값을 더해가는 방식
land에 이전행의 최댓값을 더해가면서, 가능한 경우중에서 좋은 경우만을 남기도록 탐욕적 기법을 사용
단, 이전행에서 같은 열은 제외.. 아직은 DP가 조금 어렵다

import sys

sys.setrecursionlimit(1000001)
def dfs(idx, pick, visited, ret, land):
    global answer
    if pick == len(land):
        answer = max(answer, sum(ret))
        return
    for i in range(0, 4):
        if i!= idx or pick ==0: 
            visited[i] = True
            ret.append(land[pick][i])
            dfs(i,pick+1,visited,ret,land)
            ret.pop()
            

def solution(land):
    global answer
    answer = 0
    
    # (idx, pick, visited, ret, land)
    visited = [False] * len(land[0])
    ret = []
   
    dfs(0,0,visited, ret,land)
        
    return answer

"""

def solution(land):
    for i in range(0, len(land)-1):
        land[i+1][0] += max(land[i][1],land[i][2],land[i][3])
        land[i+1][1] += max(land[i][0],land[i][2],land[i][3])
        land[i+1][2] += max(land[i][0],land[i][1],land[i][3])
        land[i+1][3] += max(land[i][0],land[i][1],land[i][2])
    return max(land[len(land)-1])