"""
2636 치즈

가장자리를 확인하는게 키포인트 이다. 치즈가 아닌 곳 즉 grid의 0인 값을 탐색해 가면서 1을 만나면 탐색을 종료하는 방법으로 가장자리를 탐색한다

00000
01110
01110
01110
00000

(0,0)에서 상하 좌우로 탐색을 시작해서 1인 (1,1)을 만나면 해당 grid를 0으로 변경해주고 카운트를 증가해준다. 이런식으로 1번 탐색하면 반복하면
아래와 같이 grid를 변경할 수 있다. 여기서 c를 모두 0으로 바꿔주면 된다.

00000
0ccc0
0c1c0
0ccc0
00000

이후 c를 0으로 생각하고 다시 (0,0)에서 탐색을 시작하면 아래와 같이 가운데 1이 c2로 변경될 것 이다. 이런식으로 가장자리를 찾으면서 값을 0으로 변경해면서 걸린 시간과 개수를 리턴하면 된다.

00000
0ccc0
0c[c2]c0
0ccc0
00000


"""

from collections import deque
from time import time

R , C = map(int, input().split())

grid = []

for i in range(R):
    data = list(map(int,input().split()))
    grid.append(data)

cheese = []

def bfs():
    visited = [[False] * C for _ in range(R)]
    q = deque()
    q.append((0,0))

    visited[0][0] = True

    dr = [1,-1,0,0]
    dc = [0,0, 1,-1]

    cnt = 0
    while q:
        now_r, now_c = q.popleft()
        for i in range(4):
            next_r = now_r + dr[i]
            next_c = now_c + dc[i]
            if 0<=next_r<R and 0<=next_c<C and not visited[next_r][next_c]:
                if grid[next_r][next_c] == 1:
                    grid[next_r][next_c] = 0
                    visited[next_r][next_c] = True
                    cnt +=1
                elif grid[next_r][next_c] == 0:
                    visited[next_r][next_c] = True
                    q.append((next_r,next_c))
    cheese.append(cnt)
    return cnt

time = 0
while 1:
    if bfs()==0:
        break
    time +=1

print(time)
print(cheese[-2])