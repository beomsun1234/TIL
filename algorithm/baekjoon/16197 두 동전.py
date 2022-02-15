"""

16197 두 동전

종료 조건은 pick이 < 10 

두동전중 하나만 떨어뜨려야한다.

실수를 정말 많이 한 것 같다. 조건이 조금 많았다. 여기서 나는 처음에 # 벽인 경우 어떻게 처리 하지 생각했다. dfs였다면 쉽게 백트래킹으로 갈 수있지만 bfs로
백트래킹을 어떻게 하지 생각했다. 간단했다 만약 벽을 만나면 이전 위치로 돌아가기 위해 큐에 이전 위치 좌표를 넣어주면 된다..
0 1
0 1

1 벽 ,0 은 내가 현재 있는 위치(1,1)에서  4방향으로 갈 수 있으며 만약 벽을 만나면 board[next_r][next_c] == 1 현재 위치로 다시 돌아 와야한다.
방법은  board[next_r][next_c] == 1(벽을 만날 경우) 다음 탐색할 좌표를 현재 좌표로 넣어주면된다. 

if board[next_r][next_c] == 1:
    next_r = r
    next_c = c
    q.append((next_r, next_c))
이런식으로 해주면된다.

"""

from collections import deque

N, M = map(int,input().split())

board = []

dr = [1,-1,0,0]
dc = [0,0,1,-1]

visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
## 'o' - 동전, '.' - 빈 칸  , '#' - 벽
for i in range(N):
    data = list(input())
    board.append(data)

coin_pos = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coin_pos.append((i,j))


def bfs():
    q = deque()
    q.append((coin_pos[0][0], coin_pos[0][1], coin_pos[1][0], coin_pos[1][1],0))
    cnt= 0 
    visited[coin_pos[0][0]][coin_pos[0][1]][coin_pos[1][0]][coin_pos[1][1]] = True
    flag = 0
    answer = 0
    while q:
        pos = q.popleft()
        # pos 0,1 -> r1,c1  
        # pos 1,2 -> r2,c2
        if pos[4] >= 10:
            return -1
        for i in range(4):
            #동전 1
            next_r_1 = pos[0] + dr[i]
            next_c_1 = pos[1] + dc[i]
            #동전 2
            next_r_2 = pos[2] + dr[i]
            next_c_2 = pos[3] + dc[i]

            if 0<=next_r_1 <N and 0<=next_c_1<M and 0<=next_r_2<N and 0<=next_r_2<N and 0<=next_c_2<M:
                if not visited[next_r_1][next_c_1][next_r_2][next_c_2]:
                    if board[next_r_1][next_c_1] == "#":
                        next_r_1, next_c_1 = pos[0], pos[1]
                    if board[next_r_2][next_c_2] == "#":
                        next_r_2, next_c_2 = pos[2], pos[3]
                    visited[next_r_1][next_c_1][next_r_2][next_c_2] = True
                    q.append((next_r_1,next_c_1,next_r_2,next_c_2, pos[4]+1))
            elif 0<=next_r_2<N and 0<=next_r_2<N and 0<=next_c_2<M: 
                return pos[4] + 1
            elif 0<=next_r_1 <N and 0<=next_c_1<M:
                return pos[4] + 1
            else:
                continue


print(bfs())