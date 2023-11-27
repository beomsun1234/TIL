from collections import deque

N,M, H = map(int, input().split())

line = [[0 for j in range((N+1))] for i in range((H+1))]

# b + 1 체크해야함
for i in range(M):
    a, b = map(int, input().split())
    line[a][b] = 2   

pick = []

def check():
    ## 내려가기
    for i in range(1,N+1):
        if not climbLadder(i):
           return False
    return True

def climbLadder(number):   
    posY = 1
    posX = number
    while(posY <= H):
        # 하나 전까지 체크
        if line[posY][posX] >0:
            posX = posX+1
        elif line[posY][posX-1] > 0:
            posX = posX -1
        else:
            posX = posX
        posY +=1 
    if posX == number:
        return True
    return False

global minVal 

minVal = 1000000000
def dfs(n,y,x):
    global minVal 
    if check():
        tmp = 0
        for i in range(H+1):
            for j in range(N+1):
                if (line[i][j] == 1):
                    tmp+=1
        minVal = min(tmp, minVal)
    #문제에서 주어진 조건 - 정답은 3보다 클 수 없다.
    if n == 3 or minVal < n:
        return
    for i in range(1, H+1):
        for j in range(1, N):
            if i < y and j < x:
                continue
            if line[i][j] == 0:
                if line[i][j+1] == 0 and line[i][j-1] == 0:
                    line[i][j] = 1
                    dfs(n+1,i,j)
                    line[i][j] = 0


dfs(0,1,1)
    
if minVal <= 3:
    print(minVal)
else:
    print(-1)
