"""
1303번 전쟁 - 전투
"""

# 81 + 49 = 130 
# 1 + 64 = 65


# 대각선은 뭉쳐있다고 보지않으므로 상하좌우만

# 상하
dr = [-1,1,0,0]
# 좌우
dc = [0,0,-1,1]

N,M = map(int,input().split())

visited = [[False]*N for _ in range(M)]
grid = []
for i in range(M):
    data = list(input())
    grid.append(data)

global wCnt
global bCnt
wCnt = 0
bCnt = 0
def dfs(r,c,type):
    global wCnt
    global bCnt
    for i in range(4):
        next_r = dr[i] + r
        next_c = dc[i] + c
        if 0<=next_r<M and 0<=next_c<N:
            if not visited[next_r][next_c] and grid[next_r][next_c]==type:
                visited[next_r][next_c] = True
                if type == 'W':
                    wCnt+=1
                if type == 'B':
                    bCnt+=1
                dfs(next_r,next_c,type)

tmpW = 0
tmpB = 0
for i in range(M):
    for j in range(N):
        if grid[i][j] == 'W' and not visited[i][j]:
            wCnt +=1
            visited[i][j] = True
            dfs(i,j,'W')
            tmpW += wCnt*wCnt
            wCnt = 0
        elif grid[i][j] == 'B' and not visited[i][j]:
            bCnt +=1
            visited[i][j] = True
            dfs(i,j,'B')
            tmpB += bCnt*bCnt
            bCnt = 0

print(tmpW, tmpB)