N, K= map(int, input().split())


paper = []

for i in range(N):
    data = list(map(int,input().split()))
    paper.append(data)




# check 직선 - 위, 왼, 오, 아 4방향으로 회전가능
# pos -> 현재 위치

# 좌우반전 추가
def check_L(paper, posX, posY):
    #  .
    #  .
    #  ..
    # 밑에 두 점 중 첫 점을 시작으로 한다.
    # 위로
    sumVal = 0
    maxVal = 0
    left = 0
    right = 0
    for i in range(0,3):
        if (posY-i < 0):
            sumVal = 0
            break
        sumVal += paper[posY-i][posX]
    ## 위 방향, 왼쪽   
    if 0<= posX -1 < K:
        left = sumVal + paper[posY][posX-1]
    if 0<= posX +1 < K:
        right = sumVal + paper[posY][posX+1]
    maxVal = max(left, right ,maxVal)
    # 아래
    sumVal = 0
    left = 0
    right = 0
    for i in range(0,3):
        if (posY+i >= N ):
            sumVal = 0
            break
        sumVal += paper[posY+i][posX]
    ## 아래 방향, 왼쪽   
    if 0<= posX -1 < K:
        left = sumVal + paper[posY][posX-1]
    if 0<= posX +1 < K:
        right = sumVal + paper[posY][posX+1]
    maxVal = max(left, right ,maxVal)
    # 오른쪽
    sumVal = 0
    left = 0
    right = 0
    for i in range(0,3):
        if (posX+i >= K ):
            sumVal = 0
            break
        sumVal += paper[posY][posX+i]
    ## 오른쪽 방향, 위   
    if 0<= posY -1 < N:
        left = sumVal + paper[posY-1][posX]
    if 0<= posY +1 < N:
        right = sumVal + paper[posY+1][posX]
    maxVal = max(left, right ,maxVal)
    # 왼쪽
    sumVal = 0
    left = 0
    right = 0
    for i in range(0,3):
        if (posX-i < 0 ):
            sumVal = 0
            break
        sumVal += paper[posY][posX-i]
    ## 오른쪽 방향, 위   
    if 0<= posY -1 < N:
        left = sumVal + paper[posY-1][posX]
    if 0<= posY +1 < N:
        right = sumVal + paper[posY+1][posX]
    maxVal = max(left, right,maxVal)
    return maxVal
# 좌우반전 추가
def check_번개(paper, posX, posY): 
    #  .
    #  ..
    #   .
    # 가장 아래에 있는 점을 기준으로 위치를 지정
    # 위로
    left = 0
    right = 0
    sumVal = 0
    maxVal = 0
    if 0<= posY -2 <N:
        sumVal = paper[posY][posX] + paper[posY-1][posX]
        # 왼
        if 0 <=posX -1 < K:
            left = paper[posY-1][posX-1] + paper[posY-2][posX-1] + sumVal
        # 오
        if 0 <=posX +1 < K:
            right = paper[posY-1][posX+1] + paper[posY-2][posX+1] + sumVal
        maxval = max(max(left,right),maxVal)
    # 아래로
    left = 0
    right = 0
    sumVal = 0
    if 0<= posY +2 <N:
        sumVal = paper[posY][posX] + paper[posY+1][posX]
        # 왼
        if 0 <=posX -1 < K:
            left = paper[posY+1][posX-1] + paper[posY+2][posX-1] + sumVal
        # 오
        if 0 <=posX +1 < K:
            right = paper[posY+1][posX+1] + paper[posY+2][posX+1] + sumVal
        maxVal = max(max(left,right),maxVal)
    #오른쪽
    left = 0
    right = 0
    sumVal = 0
    if 0<= posX +2 <K:
        sumVal = paper[posY][posX] + paper[posY][posX+1]
        # 위
        if 0 <= posY -1 < N:
            left = paper[posY-1][posX+1] + paper[posY-1][posX+2] + sumVal
        # 아래
        if 0 <= posY +1 < N:
            right = paper[posY+1][posX+1] + paper[posY+1][posX+2] + sumVal
        maxVal = max(max(left,right),maxVal)
    #왼쪽
    left = 0
    right = 0
    sumVal = 0
    if 0<= posX -2 <K:
        sumVal = paper[posY][posX] + paper[posY][posX-1]
        # 위
        if 0 <=posY -1 < N:
            left = paper[posY-1][posX-1] + paper[posY-1][posX-2] + sumVal
        # 아래
        if 0 <=posY +1 < N:
            right = paper[posY+1][posX-1] + paper[posY+1][posX-2] + sumVal
        maxVal = max(max(left,right),maxVal)
    return maxVal

def check_네모(paper, posX, posY):
    # 현재 위치가 - 위 왼
    sumVal = 0
    maxVal = 0
    if 0<=posX +1 <K and 0<= posY +1 <N:
        sumVal = paper[posY +1][posX] + paper[posY][posX+1] + paper[posY+1][posX+1] + paper[posY][posX] 
    maxVal = max(sumVal,maxVal)
    # 아래 왼
    if 0<=posX +1 <K and 0<= posY -1 <N:
        sumVal = paper[posY -1][posX] + paper[posY][posX+1] + paper[posY-1][posX+1] + paper[posY][posX] 
    maxVal = max(sumVal,maxVal)
    # 위 오
    if 0<=posX -1 <K and 0<= posY +1 <N:
        sumVal = paper[posY +1][posX] + paper[posY][posX-1] + paper[posY+1][posX-1] + paper[posY][posX] 
    maxVal = max(sumVal,maxVal)
    # 아 오
    if 0<=posX -1 <K and 0<= posY -1 <N:
        sumVal = paper[posY -1][posX] + paper[posY][posX-1] + paper[posY-1][posX-1] + paper[posY][posX] 
    maxVal = max(sumVal,maxVal)
    return maxVal


def check_직선(paper, posX, posY): 
    # 위
    sumVal = 0
    maxVal = 0
    for i in range(0,4):
        if (posY-i < 0): 
            sumVal = 0
            break
        sumVal += paper[posY-i][posX]  
    maxVal = max(sumVal, maxVal)
    sumVal = 0
    # 왼
    for i in range(0,4):
        if (posX-i < 0): 
            sumVal = 0
            break
        sumVal += paper[posY][posX-i]  
    # 오
    maxVal = max(sumVal, maxVal)
    sumVal = 0
    for i in range(0,4):
        if (posX+i >= K): 
            sumVal = 0
            break
        sumVal += paper[posY][posX+i]
    maxVal = max(sumVal, maxVal)
    sumVal = 0   
    # 아
    for i in range(0,4):
        if (posY+i >= N): 
            sumVal = 0
            break
        sumVal += paper[posY+i][posX]  
    maxVal = max(sumVal, maxVal)
    return maxVal

def check_산(paper, posX, posY): 
    #   .
    #  ... 
    # 가장 왼쪽에 있는 점을 기준으로 위치를 지정
    left = 0
    right = 0
    sumVal = 0
    maxVal = 0
    # 위
    if 0 <=posY - 2 < N:
        for i in range(0,3):
            sumVal += paper[posY-i][posX]
        ## 왼
        if 0 <= posX -1 < K:
            left =  sumVal + paper[posY-1][posX-1]
        ## 오
        if 0 <= posX + 1 < K:
            right =  sumVal + paper[posY-1][posX+1]
        
        maxVal = max(left, right, maxVal)
    ## 아래
    left = 0
    right = 0
    sumVal = 0
    if 0 <=posY + 2 < N:
        for i in range(0,3):
            sumVal += paper[posY+i][posX]
        ## 왼
        if 0 <= posX -1 < K:
            left =  sumVal + paper[posY+1][posX-1]
        ## 오
        if 0 <= posX + 1 < K:
            right =  sumVal + paper[posY+1][posX+1]
        maxVal = max(left, right, maxVal)
    ##  왼쪽
    left = 0
    right = 0
    sumVal = 0
    if 0 <=posX - 2 < K:
        for i in range(0,3):
            sumVal += paper[posY][posX-i]
        ## 위
        if 0 <= posY -1 < N:
            left =  sumVal + paper[posY-1][posX-1]
        ## 아래
        if 0 <= posY + 1 < N:
            right =  sumVal + paper[posY+1][posX-1]
        maxVal = max(left, right, maxVal)
    ##  오른쪽
    left = 0
    right = 0
    sumVal = 0
    if 0 <=posX + 2 < K:
        for i in range(0,3):
            sumVal += paper[posY][posX+i]
        ## 위
        if 0 <= posY -1 < N:
            left =  sumVal + paper[posY-1][posX+1]
        ## 아래
        if 0 <= posY + 1 < N:
            right =  sumVal + paper[posY+1][posX+1]
        maxVal = max(left, right, maxVal)
    return maxVal
    

result = 0

##
for y in range(N):
    for x in range(K):
        result = max(check_L(paper, x,y),check_네모(paper,x,y),check_번개(paper,x,y),check_직선(paper,x,y), check_산(paper, x,y), result)
        
        
print(result)        
