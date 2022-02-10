"""
17070 파이프 옮기기1

처음에 bfs로 접근했더니 88퍼쯤에서 시간초과가 발생했다... 찾아보니 파이썬으로 할 경우 bfs로 통과하기 어렵다고 한다..
이 코드를 c++로 옮기면 성공한다고 알려주었다.
다른 방법으로 dfs를 사용하기로 했다.. bfs로 작성한 코드를 dfs로 작성하니 통과했다....

from collections import deque
q = deque()
q.append((0,(0,1)))
cnt = 0
while q:
    op = q.popleft()
    if op[1][0] == N-1 and op[1][1] == N-1:
        cnt+=1
        continue
    for i in range(3):
        if op[0] == 0: #가로
            if i == 0:
                next_r = op[1][0] 
                next_c = op[1][1] +1
                if 0<=next_r <N and 0<=next_c<N and grid[next_r][next_c] == 0:
                    q.append((i,(next_r,next_c)))
            elif i == 2:#대각선
                next_r = op[1][0] +1
                next_c = op[1][1] +1
                next_r_1 = op[1][0] 
                next_c_1 = op[1][1] +1
                next_r_2 = op[1][0] +1
                next_c_2 = op[1][1] 
                if 0<=next_r <N and 0<=next_c<N and grid[next_r][next_c] == 0:
                    if grid[next_r_1][next_c_1] == 0 and grid[next_r_2][next_c_2] == 0:
                        q.append((i,(next_r,next_c)))
        elif op[0] == 1: ## 세로
            if i == 1:
                next_r = op[1][0] +1
                next_c = op[1][1] 
                if 0<=next_r <N and 0<=next_c<N and grid[next_r][next_c] == 0:
                    q.append((i,(next_r,next_c)))
            elif i == 2:#대각선
                next_r = op[1][0] +1
                next_c = op[1][1] +1
                next_r_1 = op[1][0] 
                next_c_1 = op[1][1] +1
                next_r_2 = op[1][0] +1
                next_c_2 = op[1][1] 
                if 0<=next_r <N and 0<=next_c<N and grid[next_r][next_c] == 0:
                    if grid[next_r_1][next_c_1] == 0 and grid[next_r_2][next_c_2] == 0:
                        q.append((i,(next_r,next_c)))
        elif op[0] == 2:
            if i == 0:
                next_r = op[1][0] 
                next_c = op[1][1] +1
                if 0<=next_r <N and 0<=next_c<N and grid[next_r][next_c] == 0:
                    q.append((i,(next_r,next_c)))
            elif i == 1:
                next_r = op[1][0] +1
                next_c = op[1][1] 
                if 0<=next_r <N and 0<=next_c<N and grid[next_r][next_c] == 0:
                    q.append((i,(next_r,next_c)))
            elif i == 2:#대각선
                next_r = op[1][0] +1
                next_c = op[1][1] +1
                next_r_1 = op[1][0] 
                next_c_1 = op[1][1] +1
                next_r_2 = op[1][0] +1
                next_c_2 = op[1][1] 
                if 0<=next_r <N and 0<=next_c<N and grid[next_r][next_c] == 0:
                    if grid[next_r_1][next_c_1] == 0 and grid[next_r_2][next_c_2] == 0:
                        q.append((i,(next_r,next_c)))

print(cnt)

"""
import sys
input = sys.stdin.readline
N = int(input())

grid = []


for i in range(N):
    data = list(map(int, input().split()))
    grid.append(data)


# 파이프를 2로 넣자
# 가장 처음에 파이프는 (1, 1)와 (1, 2)를 차지하고 있고, 방향은 가로이다.
"""
가로 =  가로방향 , 대각선 아래   - 2가지 이동가능
세로 =  세로방향,  대각성 아래   - 2가지 이동가능
대각선 = 가로, 세로, 대각선      - 3가지 이동 가능
"""
## 
## 0 - 가로 , 1, 세로, 2 - 대각선
def dfs(x, y, tpye):
    global cnt
    if x == n-1 and y == n-1:
        cnt += 1
        return
    if tpye == 0 or tpye == 2: # 가로
        if y + 1 < n:
            if a[x][y+1] == 0:
                dfs(x, y+1, 0)
    if tpye == 1 or tpye == 2: #세로
        if x + 1 < n:
            if a[x+1][y] == 0:
                dfs(x+1, y, 1)
    if tpye == 0 or tpye == 1 or tpye == 2: #대각선
        if x + 1 < n and y + 1 < n:
            if a[x+1][y] == 0 and a[x][y+1] == 0 and a[x+1][y+1] == 0:
                dfs(x+1, y+1, 2)


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
dfs(0, 1, 0)
print(cnt)