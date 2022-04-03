"""
프로그래머스 2019 카카오 개발자 겨울 인턴십
 불량사용자

"""

from copy import deepcopy
def checkId(ban_id, user_id):
    if len(ban_id) != len(user_id):
        return False
    for i in range(len(ban_id)):
        if ban_id[i]!= '*' and ban_id[i] != user_id[i]:
            return False
    return True
def dfs(pick,ban_id,user_id,tmp,ans,visited):
    if pick == len(ban_id):
        tt = sorted(deepcopy(tmp))
        if tt not in ans:
            ans.append(tt)
        return
    for i in range(len(user_id)):
        if not visited[i] and checkId(ban_id[pick],user_id[i]):
            visited[i] = True
            tmp.append(user_id[i])
            dfs(pick+1,ban_id, user_id, tmp, ans, visited)
            visited[i] = False
            tmp.pop()
            
def solution(user_id, banned_id):
    answer = 0
    tmp = []
    ans = []
    visited = [False] * len(user_id)
    dfs(0,banned_id, user_id, tmp, ans,visited)
    print(ans)
    return len(ans)