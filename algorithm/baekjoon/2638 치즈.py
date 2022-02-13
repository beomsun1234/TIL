""""
2638 치즈
bfs로 가장자리를 찾고 
찾은 가장자리의 변이 2개 이상 공기와 노출되어있다면 c로 변경 간단할 듯??

위 방법대로 접근하니 정답을 도출 할 수 있었다.

"""

from collections import deque
N, M = map(int,input().split())

grid = []

for i in range(N):
    data = list(map(int,input().split()))
    grid.append(data)

dr = [1,-1,0,0]
dc = [0,0, 1,-1]

# 치즈가 전부 녹았는지 확인
def isAllMelt():
    for i in range(N):
        for j in range(M):
            if grid[i][j] != 0:
                return False
    return True

# 치즈 녹이기 grid[i][j]가 3 이상이면  2변 이상이면 공기와 접촉
#  2일 경우는 2번 이상 접촉안했으므로 다시 치즈로 변환
def melt():
    for i in range(N):
        for j in range(M):
            if grid[i][j] >= 3:
                grid[i][j] = 0
            elif grid[i][j] == 2:
                grid[i][j] = 1


def bfs(start_r, start_c):
    visited = [[False] * M for _ in range(N)]
    q = deque()
    q.append((start_r,start_c))
    while q:
        now_r, now_c = q.popleft()
        for i in range(4):
            next_r = now_r + dr[i]
            next_c = now_c + dc[i]
            if 0<=next_r<N and 0<=next_c <M and not visited[next_r][next_c]:
                if grid[next_r][next_c] != 0:
                    grid[next_r][next_c] +=1
                elif grid[next_r][next_c] == 0:
                    visited[next_r][next_c] = True
                    q.append((next_r, next_c))
    melt()
    return isAllMelt()
time = 0
while 1:
    if bfs(0,0):
        time+=1
        break
    time+=1
    
print(time)