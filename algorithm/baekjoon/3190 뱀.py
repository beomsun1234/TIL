"""
3190 뱀
"""
# 
from collections import deque
#보드크기
N = int(input())
board = [[0] *N for _ in range(N)]
#사과 개수
K = int(input())

# 뱀은 1 -1은 사과
for i in range(K):
    r,c = map(int,input().split())
    board[r-1][c-1] = -1

board[0][0] = 1
snake_pos = deque()
snake_pos.append((0,0))
#방향전향 횟수
L = int(input())

## L -> 왼쪽 90도 , R -> 오른쪽 90도
d = {}
for i in range(L):
    data = input().split()
    d[int(data[0])]= data[1]
# 방향 바꾸기
def changeDir(look_ahead, dd):
    if look_ahead == 0:
        if dd == 'L':
                look_ahead  = 2
        elif dd == 'D':
                look_ahead = 3
    elif look_ahead == 1:
        if dd == 'L':
            look_ahead  = 3
        elif dd == 'D':
            look_ahead = 2

    elif look_ahead == 2:
        if dd == 'L':
            look_ahead  = 1
        elif dd == 'D':
            look_ahead = 0
    elif look_ahead == 3:

        if dd == 'L':
            look_ahead  = 0
        elif dd == 'D':
            look_ahead = 1
    return look_ahead
# 0 = >, 1 = < , 2 = ^ , 3 = 아래보고있다
look_ahead = 0
time = 0
now_r, now_c = 0,0
while 1:
    time+=1     
    if look_ahead == 0:#오른쪽 보고있다
        now_c+=1
    elif look_ahead == 1: # 왼쪽 보고있
        now_c -=1
    elif look_ahead == 2: # 위에 보고있다
        now_r -=1
    elif look_ahead == 3: # 아래 보고있다.
        now_r+=1
    next_r = now_r
    next_c = now_c
    if time in d:
        dd = d.get(time)
        look_ahead = changeDir(look_ahead, dd)
    if not 0<=next_r <N or not 0<= next_c<N:
        break
    if (next_r,next_c) in snake_pos:
        break
    # 사과를 먹었다면?
    elif board[next_r][next_c] == -1:
        # 사과를 없앤다
        board[next_r][next_c] = 0
        # 뱀길이 추가
        snake_pos.append((next_r,next_c))
        continue
    # 사과를 안먹었다면?
    elif board[next_r][next_c] == 0:
        # 길이 감소
        snake_pos.append((next_r,next_c))
        snake_pos.popleft()
        continue
     

print(time)
