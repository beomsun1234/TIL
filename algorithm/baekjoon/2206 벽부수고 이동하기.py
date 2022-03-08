"""
2206 벽부수고 이동하기
"""
import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0]
n, m = map(int, input().split())
dy = [0, 0, -1, 1]
visit = [[[0] * 2 for i in range(m)] for i in range(n)]
visit[0][0][1] = 1 ## wall=1이면 벽을 아직 안부순상태

def bfs():
    q = deque()
    q.append([0, 0, 1])  ## wall=1이면 벽을 아직 안부순상태
    while q:
        x, y, wall = q.popleft()
        if x == n - 1 and y == m - 1:
            return visit[x][y][wall]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if s[nx][ny] == 1 and wall == 1: ## 벽이고 아직 벽을 안부쉈다면?
                    visit[nx][ny][0] = visit[x][y][1] + 1 #부순상태로 바꿔줌
                    q.append([nx, ny, 0])
                elif s[nx][ny] == 0 and visit[nx][ny][wall] == 0:
                    visit[nx][ny][wall] = visit[x][y][wall] + 1
                    q.append([nx, ny, wall])

    return -1
s = []
for i in range(n):
    s.append(list(map(int, list(input().strip()))))
print(bfs())
print(visit)