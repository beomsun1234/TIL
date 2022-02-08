"""
14502 - 연구소

벽을 3개를 0인지점에 랜덤으로 3개 세우고 그중 안전영역이 가장 큰 영역의 수를 출력하면 될 것 같다.
처음 생각했던 방식으로 구현하니 정답이다. 3개의 벽을 세우고 바이러스를 퍼트린 뒤 이후 안전영역의 최대값을 구하면 된다.

"""
from collections import deque
N, M = map(int, input().split())
grid = []

for i in range(N):
    data = list(map(int,input().split()))
    grid.append(data)
visited = [[False]*M for _ in range(N)]
global ret
ret = 0
global cnt
global zero_cnt
zero_cnt = 0

# 바이러스가 퍼지기 전 안전영역 구하기
for i in grid:
    zero_cnt+= i.count(0)
zero_cnt -=3
dr = [1,-1,0,0]
dc = [0,0,1,-1]
## 바이러스 퍼트리기
def bfs(start_r, start_c, visited):
    global cnt
    q = deque()
    q.append((start_r, start_c))
    visited[start_r][start_c] = True
    while q:
        now_r, now_c = q.popleft()
        for i in range(4):
            next_r = now_r + dr[i]
            next_c = now_c + dc[i]
            if 0<=next_r<N and 0<=next_c <M and not visited[next_r][next_c] and grid[next_r][next_c] == 0:
                visited[next_r][next_c] = True
                cnt+=1
                q.append((next_r, next_c))
                
## 0인지점에 벽 3개 세우기    
def dfs(pick, visited):
    global cnt
    global ret
    if pick == 3:
        cnt =0
        visited = [[False]*M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 2:
                    bfs(i,j,visited)
        ## 안전영역 계산 및 최대 값 구하기
        ### 안전영역은 0인 지역의 개수에서 바이러스가 퍼진 지역의 개수를 빼주면 된다.
        ret = max(ret,zero_cnt-cnt)
        return
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                grid[i][j] = 1
                dfs(pick+1,visited)
                grid[i][j] = 0
dfs(0,visited)
print(ret)