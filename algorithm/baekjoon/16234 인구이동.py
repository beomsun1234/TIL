"""
16234 인구이동
"""

from collections import deque
N, L, R = map(int,input().split())
grid = []
for i in range(N):
    data = list(map(int,input().split()))
    grid.append(data)
dr = [1,-1,0,0]
dc = [0,0,1,-1]
visited = [[False]*N for _ in range(N)]
# 연합구성하기
def bfs(r,c):
    q = deque()
    q.append((r,c))
    tmp_union = []
    while q:
        now_r, now_c = q.popleft()
        for i in range(4):
            next_r = dr[i] + now_r 
            next_c = dc[i] + now_c
            if 0<= next_r < N and 0<=next_c <N:
                if not visited[next_r][next_c]:
                    # 연합 구성 조건에 부합한다면 연합 하기
                    if L<=abs(grid[next_r][next_c] - grid[now_r][now_c])<=R:
                        visited[next_r][next_c] = True
                        q.append((next_r,next_c))
                        tmp_union.append((next_r,next_c))
    return tmp_union

time = 0
flag = 0
while 1:
    time+=1
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union_list = bfs(i,j)
                # 연합이 구성됐다면 인구 이동
                if len(union_list) >0:
                    val = 0
                    flag += 1
                    cnt = len(union_list)
                    for r,c in union_list:
                        val+=grid[r][c]
                    val = val//cnt
                    # 인구 이동
                    for r,c in union_list:
                        grid[r][c] = val   
                        
    #연합을 한번도 구성하지 못했다면 종료
    if flag == 0:
        break   
    flag = 0
    visited = [[False]*N for _ in range(N)]

print(time-1)