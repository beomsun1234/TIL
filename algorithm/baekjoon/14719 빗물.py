"""
14719 빗물

간단했다. 나는 2차원 세계 블록을 주어진 것 과 반대로 설정하였다. 높이를 컬럼으로 보고, 넓이를 로우로 변환하여 풀었다.

로직은 간단하다. 우선 주어진 블록의 높이들을 가지고 2차원세계에 블록을 쌓는다. 블록을 쌓고 가장 낮은 블록순으로 정렬한다.
정렬한 블록을 가지고(인덱스포함) 고인 빗물을 계산한다.

만약 현재칸에서 블록이 없을때 조건을 만족하면 빗물이 고일수 있다. 만약 현재칸을 기준으로 왼쪽 부분과 오른쪽 부분을 확인하여(같은 높이) 해당 부분에 빗물이 놓일 수 있다면
빗물을 놓는다(grid[i][j]=2). 해당 방식으로 주어진 블록들을 다 확인 하여 빗물을 놓고 쌓인 빗물의 값을 리턴하면 된다. 

"""

W, H = map(int,input().split())

grid = [[0]*W for _ in range(H)]


# 각 빗물
w_h = list(map(int,input().split()))
tmp = []
for idx,hh in enumerate(w_h):
    tmp.append((hh,idx))
    for i in range(0,hh):
        grid[idx][i] = 1
tmp.sort()
for hh,idx in tmp:
    for i in range(W):
        if grid[idx][i] == 0:
            #왼쪽
            flag = 0
            for j in range(idx-1, -1,-1):
                if grid[j][i] == 1:
                    flag +=1
                    break
            #오른쪽
            for j in range(idx+1, H):
                if grid[j][i] == 1:
                    flag +=1
                    break
            if flag == 2:
                grid[idx][i]=2

answer = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == 2:
            answer+=1

print(answer)

            
