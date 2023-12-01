N, M = map(int, input().split())
import copy
board = []
tmp_board = []
for i in range(N):
    board.append(list(map(str,input())))

tmp_board = copy.deepcopy(board)

redPos = []
tmp_r = []
bluePos = []
tmp_b = []
targetPos = []
for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            tmp_board[i][j] = "."
            redPos.append([i,j])
        elif board[i][j] == "B":
            tmp_board[i][j] = "."
            bluePos.append([i,j])
        elif board[i][j] == "O":
            targetPos.append([i,j])

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 상,하, 좌,우
pick = []

global minVal
minVal = 100000000000

def checkOutBound(x,y) -> bool:
    if 0<= x <N and 0<= y <M:
        return True
    return False

posR = []
posB = []

# 1-red,2- blue
def moveOrder(dir, posR, posB)->str:
    if dir == 0:
        #위 check
        # y축이 다르면 동일선상에 있지 않다. 그럴경우 red가 먼저
        if posR[-1][1] != posB[-1][1]:
            return "red"
        else:
            # 동일선상에서 값이 크면 밑에있다.
            if posR[-1][0] > posB[-1][0]:
                return "blue"
            else:
                return "red"
    elif dir == 1:
        #아래 check
        # y축이 다르면 동일선상에 있지 않다. 그럴경우 red가 먼저
        if posR[-1][1] != posB[-1][1]:
            return "red"
        else:
            # 동일선상에서 값이 크면 밑에있다.
            if posR[-1][0] > posB[-1][0]:
                return "red"
            else:
                return "blue"
    elif dir == 2:
        #왼쪽 check
        # x축이 다르면 동일선상에 있지 않다. 그럴경우 red가 먼저
        if posR[-1][0] != posB[-1][0]:
            return "red"
        else:
            # 동일선상에서 값이 크면 오른쪽.
            if posR[-1][1] > posB[-1][1]:
                return "blue"
            else:
                return "red"
    elif dir == 3:
        #왼쪽 check
        # x축이 다르면 동일선상에 있지 않다. 그럴경우 red가 먼저
        if posR[-1][0] != posB[-1][0]:
            return "red"
        else:
            # 동일선상에서 값이 크면 오른쪽.
            if posR[-1][1] > posB[-1][1]:
                return "red"
            else:
                return "blue"
                 


def move(dir, pos, b, color):
    nowX = pos[-1][0]
    nowY = pos[-1][1]
    if tmp_board[nowX][nowY] == "O":
        return nowX, nowY, True
    
    nx = nowX
    ny = nowY
    moveCnt = 0
    target = False
    while 1:
        nx = nowX + dx[dir]
        ny = nowY + dy[dir]
        if not checkOutBound(nx,ny):
            break
        #장애물
        if b[nx][ny] == "#":
            break
        if b[nx][ny] == "B":
            break
        if b[nx][ny] == "R":
            break
        if b[nx][ny] == "O":
            target = True
            nowX = nx
            nowY = ny
            break
        moveCnt +=1
        nowX = nx
        nowY = ny

    if b[nowX][nowY] != "O":
        if color == "red":
            b[nowX][nowY] = "R"
        else:
            b[nowX][nowY] = "B"
        if moveCnt > 0:
            b[pos[-1][0]][pos[-1][1]] = "."
    
    return nowX,nowY,target


def dfs(n,pre,posR, posB):
    global minVal
    if n>=11:
        return
    if minVal <= n:
        return
    for i in range(4):
        # 0 상, 1 - 하, 2- 좌, 3-우
        if i == pre:
            continue
        c = moveOrder(i, posR=posR, posB=posB)

        b = copy.deepcopy(tmp_board)

        if c == "red":
            nRedX,  nRedY, tr= move(i, posR,b,"red")
            nBlueX, nBlueY, tb =   move(i, posB, b,"blue")
            if tr and not tb:
                minVal = min(minVal, n)
                continue
        else:
            nBlueX, nBlueY, tb =   move(i, posB, b,"blue")
            nRedX,  nRedY,  tr= move(i, posR,b,"red") 
            if not tb:
                if tr:
                    minVal = min(minVal, n)
                    continue
    
        posR.append([nRedX,nRedY])
        posB.append([nBlueX,nBlueY])
        dfs(n+1, i, posR,posB)
        posR.pop()
        posB.pop()

posR.append([redPos[0][0], redPos[0][1]])
posB.append([bluePos[0][0], bluePos[0][1]])
dfs(1,-1, posR, posB)

if minVal > 10:
    print(-1)
else:
    print(minVal)
