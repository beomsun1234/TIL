"""
17144  미세먼지 안녕!

간단했다. 주어진 내용대로 구현하면 됐다.
주의할 점은 확산 할 때 확산의 원인이 되는 지역의 값을 가지고 있어야한다. 조금 까다로운 점이 확산 이 후 청소가 살짝 까다로웠다. 디버깅을 많이 했다.
공기 청정기 작동 시 배열 회전을 적용하면 정답을 도출 할 수 있다.
"""


R,C,T = map(int, input().split())
import math
"""
확산되는 양은 Ar,c/5

미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수)
"""
grid = []
grid_copy = [[0]* C for _ in range(R)]
for i in range(R):
    data = list(map(int,input().split()))
    grid.append(data)

# grid[r][c] == -1 -> 공기청소기
dr = [1,-1,0,0]
dc = [0,0,1,-1]
air_clear_pos = []
## 미세먼지 확산 
def diffusion(r,c,dust_cnt):
    cnt = 0
    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0<=next_r<R and 0<=next_c < C and grid[next_r][next_c] > -1:
            cnt+=1
            grid[next_r][next_c] += math.trunc(dust_cnt/5)
    grid[r][c]-=math.trunc(dust_cnt/5)*cnt

## 공기청정기 작동
def clearDust():
    ## 위방향
    up_r = air_clear_pos[0][0]
    # 4가지 방향으로 돈다
    # 1 바텀 라이트
    for i in range(2,C):
        tmp = grid[up_r][i-1]
        grid[up_r][i-1] = 0
        grid_copy[up_r][i] = tmp
    # #2 바텀 업
    for i in range(up_r,0,-1):
        tmp = grid[i][C-1]
        grid[i][C-1] = 0
        grid_copy[i-1][C-1] = tmp
    # #3 탑 레프트
    for i in range(C-2,-1,-1):
        tmp = grid[0][i+1]
        grid[0][i+1] = 0
        grid_copy[0][i] = tmp
    # #4 탑 다운
    for i in range(1, up_r+1):
        tmp = grid[i-1][0]
        grid[i-1][0] = 0
        grid_copy[i][0] = tmp
    #### 아래방향
    down_r = air_clear_pos[1][0]
    # 1 탑 라이트
    for i in range(2,C):
        tmp = grid[down_r][i-1]
        grid[down_r][i-1] = 0
        grid_copy[down_r][i] = tmp
    # #2 탑 다운
    for i in range(down_r+1,R):
        tmp = grid[i-1][C-1]
        grid[i-1][C-1] = 0
        grid_copy[i][C-1] = tmp
    # #3 바텀 레프트
    for i in range(C-2,-1,-1):
        tmp = grid[R-1][i+1]
        grid[R-1][i+1] = 0
        grid_copy[R-1][i] = tmp
    # # #4 바텀 업
    for i in range(R-1, down_r,-1):
        tmp = grid[i][0]
        grid[i][0] = 0
        grid_copy[i-1][0] = tmp

## 적용하기
def adjust():
    for i in range(R):
        for j in range(C):
            if grid_copy[i][j] >0:
                grid[i][j] = grid_copy[i][j]
    ## 공기청정기 재설치
    grid[air_clear_pos[0][0]][air_clear_pos[0][1]] = -1
    grid[air_clear_pos[1][0]][air_clear_pos[1][1]] = -1

for k in range(T):
    dust = []
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] > 0:
                dust.append((i,j,grid[i][j]))
            elif grid[i][j] == -1:
                air_clear_pos.append((i,j))

    for rr,cc,d_c in dust:
        diffusion(rr,cc,d_c)
    clearDust()
    adjust()
    grid_copy = [[0]* C for _ in range(R)]

ret = 0
for i in range(R):
    for j in range(C):
        if grid[i][j] >0:
            ret+=grid[i][j]
print(ret)