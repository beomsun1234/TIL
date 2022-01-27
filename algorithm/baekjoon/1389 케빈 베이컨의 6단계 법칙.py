"""
bfs 사용 1389 - 케빈 베이컨의 6단계 법칙
자기 자신을 제외하고 가장 적게 방문하는 횟수
"""
from collections import deque

N, M = map(int,input().split())

relation = []
for i in range(N+1):
    relation.append([])

for i in range(M):
    n1, n2 = map(int, input().split())
    relation[n1].append(n2) 
    relation[n2].append(n1)

visited = set()


def bfs(start,end):
    q = deque()
    q.append((start,0))
    visited.add(start)
    while q:
        node , cnt = q.popleft()
        if node == end:
            return cnt
        for e in relation[node]:
            if e not in visited:
                q.append((e,cnt+1))
        

ret = {}
minVal = 10000
for i in range(1,N+1):
    now_sum = 0
    for j in range(1,N+1):
        if i!=j:
            now_sum += bfs(i,j)
            visited = set()

    minVal = min(minVal, now_sum) 
    if now_sum not in ret:
        ret[now_sum] = [i]
    else:
        ret[now_sum].append(i)

print(ret.get(minVal)[0])