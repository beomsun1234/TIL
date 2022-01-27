"""
15686 - 치킨 배달

"""

N, M = map(int, input().split())


chickenZipCombi = []

chickenZip = []
house = []
grid = []
for i in range(N):
    data = list(map(int,input().split()))
    grid.append(data)

for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            chickenZip.append((i,j))
        if grid[i][j] == 1:
            house.append((i,j))


global minVal
minVal = 99999
## 치킨집 뽑기
def dfs(pick,idx):
    global minVal
    if pick == M:
        ## 뽑은 치킨집을 바탕으로 완탐을 돌려서 거리를 구한다
        city_chicken_dis = 0
        for h in house:
            house_chicken_dis = 99999
            ## 집에서 가까운 치킨집 거리 계산
            for k in range(M):
                house_chicken_dis = min(house_chicken_dis, abs(h[0]-chickenZipCombi[k][0]) + abs(h[1]- chickenZipCombi[k][1]))
            city_chicken_dis += house_chicken_dis
        minVal = min(minVal, city_chicken_dis)
        return  
    for i in range(idx,len(chickenZip)):
        chickenZipCombi.append(chickenZip[i])
        dfs(pick+1, i+1)
        chickenZipCombi.pop()

dfs(0,0)

print(minVal)