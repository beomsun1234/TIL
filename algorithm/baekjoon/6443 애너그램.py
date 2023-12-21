N = int(input())


def dfs(n, t):
    if n == len(s):
        print(t)
        return
    for i in visited:
        if visited[i] ==0:
            continue
        visited[i] -=1
        t += i
        dfs(n+1, t)
        t = t[:-1]
        visited[i] +=1

for i in range(N):
    s = input()
    tmp = ""
    t=list(s)
    t.sort()
    s="".join(t)
    visited = {}
    for ss in s:
        if ss not in visited:
            visited[ss] = 1
        else:
            visited[ss] +=1
        
    dfs(0, tmp)

"""
시간초과 코드
N = int(input())


def dfs(n, t):
    if n == len(s):
        ans.add(t)
        return
    for i in range(len(s)):
        if visited[i]:
            continue
        visited[i]= True
        t += s[i]
        dfs(n+1, t)
        t = t[:-1]
        visited[i]= False

for i in range(N):
    s = input()
    tmp = ""
    t=list(s)
    t.sort()
    s="".join(t)
    ans = set()
    visited = [False] * len(s)
    dfs(0, tmp)
    ret = []
    for i in ans:
        ret.append(i)
    ret.sort()
    for i in ret:
        print(i)


"""
