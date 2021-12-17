"""
월간 코드 챌린지 level1 두 개 뽑아서 더하기
"""

def dfs(pick,idx,ret,visited,numbers,answer):
    if pick == 2:
        answer.add(sum(ret))
        return
    for i in range(idx,len(numbers)):
        if not visited[i]:
            visited[i] = True
            ret.append(numbers[i])
            dfs(pick+1,i,ret,visited,numbers,answer)
            visited[i] = False
            ret.pop()
            
def solution(numbers):
    answer = set()
    numbers.sort()
    ret = []
    visited = [False] * len(numbers)
    dfs(0,0,ret,visited,numbers,answer)
    ret = list(answer)
    ret.sort()
    return ret
    