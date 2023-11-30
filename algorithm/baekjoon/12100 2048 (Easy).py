from collections import deque
import copy
N = int(input())
global result
result = 0
board = []
tmp_board = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]


for i in range(N):
    board.append(list(map(int,input().split())))



pick = []

def combineBlock(block) -> list:
    cBlock = []
    pos = 0
    while pos < len(block):
            #내 다음이 존재하면
            if pos+1< len(block):
                # 그 다음 값이 현재와 같다면 합친다.
                if block[pos] == block[pos+1]:
                    cBlock.append(block[pos] + block[pos+1])
                    pos +=2
                else:
                    cBlock.append(block[pos])
                    pos+=1
            else:
                cBlock.append(block[pos])
                pos+=1
    return cBlock

def 상(tmp_board):
    for y in range(N):
        block = []
        for x in range(N):
            if tmp_board[x][y] != 0:
                block.append(tmp_board[x][y])
        cBlock = combineBlock(block)
        
        for i in range(len(cBlock)):
            tmp_board[i][y] = cBlock[i]
        for i in range(len(cBlock),N):
            tmp_board[i][y] = 0          
    return
def 하(tmp_board):
    for y in range(N):
        block = []
        for x in range(N-1, -1,-1):
            if tmp_board[x][y] != 0:
                block.append(tmp_board[x][y])

        cBlock = combineBlock(block)
    
        for i in range(len(cBlock)):
            tmp_board[(N-1)-i][y] = cBlock[i]
        for i in range(len(cBlock),N):
            tmp_board[(N-1)-i][y] = 0     
    return
def 좌(tmp_board):
    for x in range(N):
        block = []
        for y in range(N-1, -1,-1):
            if tmp_board[x][y] != 0:
                block.append(tmp_board[x][y])

        cBlock = combineBlock(block)
                
            # 존재하지않다면 마지막이라는 소리
        for i in range(len(cBlock)):
            tmp_board[x][i] = cBlock[i]
        for i in range(len(cBlock),N):
            tmp_board[x][i] = 0     
    return
def 우(tmp_board):
    for x in range(N):
        block = []
        for y in range(N):
            if tmp_board[x][y] != 0:
                block.append(tmp_board[x][y])

        cBlock = combineBlock(block)

        for i in range(len(cBlock)):
            tmp_board[x][(N-1)-i] = cBlock[i]
        for i in range(len(cBlock),N):
            tmp_board[x][(N-1)-i] = 0     
    return
    
def moveBlock(pick):
    global result
    tmp_board = copy.deepcopy(board)
    #print("----------------------------")
    #print("pick -> ", pick )
    # 0 - 상, 1 - 하, 2 - 좌, 3 - 우
    for p in pick:
        # 이동시키고
        if p ==0:
            상(tmp_board)
        elif p==1:
            하(tmp_board)
        elif p==2:
            좌(tmp_board)
        elif p==3:
            우(tmp_board)
        # 합친다.
    maxVal = 0
    for i in range(N):
        for j in range(N):
            #print(tmp_board[i][j], end=" ")
            maxVal = max(tmp_board[i][j], maxVal) 
        #print("")
    result = max(maxVal, result)
    #print("----------------------------")

# 최대 5번 움직임
# 상,하,좌,우
def dfs(n):
    if n == 5:
        moveBlock(pick)
        return
    moveBlock(pick)
    for i in range(4):
        pick.append(i)
        dfs(n+1)
        pick.pop()

dfs(0)

print(result)
