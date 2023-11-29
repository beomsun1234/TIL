from collections import deque
import copy
N, M = map(int, input().split())

lab = []

for i in range(N):
    lab.append(list(map(int,input().split())))


global emptySpace
emptySpace = 0

combi = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 1:
            lab[i][j] = "-"
        elif lab[i][j] == 2:
            lab[i][j] = "*"
            combi.append([i,j,0])
        else:
            emptySpace +=1

global minVal
minVal = 100000000000000

dx = [1,-1,0,0]
dy = [0,0,1,-1]

pick = []
tmp_lab = []

def move(pick, val, tmp_lab):
    global emptySpace
    global minVal
    q = deque()
    space = 0
    time = [[-1 for _ in range(N)] for _ in range(N)]
    for val in pick:
        q.append(val)
        time[val[0]][val[1]] = 0
    while q:
        pos = q.popleft()
        x = pos[0]
        y = pos[1]
        tt = pos[2]
        if tt >= minVal:
            break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx < N and 0<= ny< N:
                if time[nx][ny] != -1:
                    continue
                if tmp_lab[nx][ny] == "-":
                    continue
                if(tmp_lab[nx][ny]==0 or tmp_lab[nx][ny]=="*") :
                    if tmp_lab[nx][ny]==0:
                        space +=1
                    time[nx][ny] = time[x][y] +1
                    q.append([nx,ny, tt +1] )

    if space == emptySpace:
        t = 0
        for i in range(N):
            for j in range(N):
                if(tmp_lab[i][j]==0):
                    if time[i][j] == -1:
                        t = 100000000000000
                        break
                    t = max(time[i][j],t) 
    else:
        t = 100000000000000
    minVal = min(t, minVal)   

def dfs(n,pick, idx):
    global minVal
    if n == M:
        tmp_lab = copy.deepcopy(lab)
        for i in range(M):
            x = pick[i][0]
            y = pick[i][1]
            tmp_lab[x][y] = "b"
        move(pick,0,tmp_lab)
        return
    for i in range(idx,len(combi)):
        pick.append(combi[i])
        dfs(n+1, pick, i+1)
        pick.pop()

    """
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and lab[i][j] == "*":
                visited[i][j] = True
                pick.append([i,j,0])
                dfs(n+1, pick)
                pick.pop()
                visited[i][j] = False
     """           
dfs(0,pick,0)

if minVal == 100000000000000:
    print(-1)
else:
    print(minVal)
