"""
백준 - 토마토 7569
처음에 dfs로 접근하니 풀리지 않았다.... bfs로 접근하니 정답을 맞출수 있었다.

3차원 배열을 만들고 6가지 방향으로 탐색해서 몇일 걸리는지 체크하고 가장 오래걸린 시간을 리턴하면 된다.


"""
from collections import deque

m,n,h = map(int, input().split())

grid = []
visited = []
tmp = []
for hh in range(h):
    grid.append([])
    visited.append([])
    for nn in range(n):
        for mm in range(m):
            tmp.append(False) 
        visited[hh].append(tmp)
        tomato = list(map(int, input().split()))
        tmp = []
        grid[hh].append(tomato)

#위 ,아래   
dh = [1,-1,0,0,0,0]
# 앞,뒤
dr = [0,0,1,-1,0,0]
# 왼,오
dc = [0,0,0,0,1,-1]

q = deque()
# 자라난 토마토의 죄표를 얻어온다.
for hhh in range(h):
    for nnn in range(n):
        for mmm in range(m):
            if grid[hhh][nnn][mmm] == 1:
                q.append((hhh,nnn,mmm))

#토마토가 자란곳을 기준으로 주변을 탐색한다.
while q:
    now_h, now_n, now_m = q.popleft()
    for i in range(6):
        next_h = now_h+ dh[i]
        next_n = now_n + dr[i]
        next_m = now_m + dc[i]
        if next_h >= h or next_h < 0:
            continue
        if next_n >= n or next_n<0:
            continue
        if next_m >= m or next_m<0:
            continue
        if grid[next_h][next_n][next_m] == 0:
            grid[next_h][next_n][next_m] = grid[now_h][now_n][now_m] +1
            q.append((next_h,next_n,next_m))

maxVal = 0
flag = 0
## 토마토가 익은 후 그리드를 확인해서 토마토가 익기 위해 걸린 최대 일 수를 찾는다. 
for g in grid:
    for gg in g:
        for ggg in gg:
            if ggg == 0:
                flag=1
                break
            maxVal = max(maxVal,ggg)


if flag == 1:
    print(-1)
else:
    print(maxVal-1)