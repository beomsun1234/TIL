"""
2583 영역 구하기

간단했다. 영역을 그려준(grid[y][x]=1) 다음 dfs로 grid가 0이 지점을 탐색해주면 됐다. 넓이는 0인 영역의 grid의 칸의 개수를 구하면 된다.  

"""
import sys
sys.setrecursionlimit(10000)

dr = [1,-1,0,0]
dc = [0,0,-1,1]

M,N, K = map(int, input().split())

grid = [[0]* N for _ in range(M)]

visited = [[0] * N for _ in range(M)]

global area
area = 0

def dfs(r,c):
    global area
    for i in range(4):
        nr =  r + dr[i]
        nc = c + dc[i]
        if 0<=nr<M and 0<=nc<N and not visited[nr][nc] and grid[nr][nc] == 0:
            visited[nr][nc] = True
            area+=1
            dfs(nr,nc)
            


for i in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for j in range(y1,y2):
        for k in range(x1,x2):
            grid[j][k] = 1
cnt =0
ret = []
for i in range(M):
    for j in range(N):
        if grid[i][j] == 0 and not visited[i][j]:
            area +=1
            cnt+=1
            visited[i][j] = True
            dfs(i,j)
            ret.append(area)
            area = 0

print(cnt)
ret.sort()
answer = ""
for idx,i in enumerate(ret):
    answer += str(i)
    if idx < len(ret):
        answer += " "
print(answer)