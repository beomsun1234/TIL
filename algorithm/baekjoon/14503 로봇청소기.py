"""
백준 - 14503 로봇 청소기

"""
##
##
#  d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽
# 1. 현재 위치를 청소한다.
# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색한다.
#   a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
#   b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
#   c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
#   d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.

from collections import deque

n,m = map(int, input().split())
startR , startC, startD = map(int,input().split())

grid = []

for i in range(n):
    data = list(map(int,input().split()))
    grid.append(data)

# 북동남서
dr = [-1,0,1,0]
dc = [0,1,0,-1]

#d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽
def change(dd):
    if dd == 0:
        return 3
    if dd == 1:
        return 0
    if dd == 2:
        return 1
    if dd == 3:
        return 2

def back(dd):
    if dd == 0:
        return 2
    elif dd == 1:
        return 3
    elif dd == 2:
        return 0
    elif dd == 3:
        return 1

q = deque()
answer = 0
q.append((startR,startC,startD))
grid[startR][startC] = 2
flag = 0
# 2= 청소 완료 0은 청소 x, 1은벽
while q:
    now_r, now_c, now_d = q.popleft()
    ## 왼쪽 부터 탐색
    temp_d = now_d
    for i in range(4):
        temp_d = change(temp_d)
        #현재 방향을 기준으로 왼쪽에서 부터 인접한 칸 탐색
        next_r = dr[temp_d] + now_r
        next_c = dc[temp_d] + now_c
        #a
        if 0 <= next_r <=n and 0<=next_c <= m and grid[next_r][next_c] ==0:
            answer+=1
            grid[next_r][next_c] = 2
            q.append((next_r,next_c, temp_d))
            break
        
        # c
        elif i ==3: # 갈곳x
            next_r = dr[back(now_d)] + now_r
            next_c = dc[back(now_d)] + now_c
            q.append((next_r,next_c, now_d))

            if grid[next_r][next_c] == 1:
                flag = 1
                break

    if flag == 1:
        break
    
print(answer+1)