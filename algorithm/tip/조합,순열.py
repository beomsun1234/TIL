## 조합
l = ['a', 'b', 'c', 'd']
n = len(l)
r = 2
answer = []

def dfs2(idx, list):
    if len(list) == r:
        answer.append(list[:])
        return

    for i in range(idx, n):
        dfs2(i+1,list+[l[i]])

dfs2(0, [])
print(answer)
## 순열
l = ['a', 'b', 'c']
visited = [0 for _ in range(len(l))]
answer = []

def dfs(cnt, list):
    if cnt == len(l):
        answer.append(list[:])
        return

    for i, val in enumerate(l):
        if visited[i] == 1:
            continue
        list.append(val)
        visited[i] = 1

        dfs(cnt+1, list)
       
        list.pop()
        visited[i] = 0

dfs(0, [])
print(answer)
