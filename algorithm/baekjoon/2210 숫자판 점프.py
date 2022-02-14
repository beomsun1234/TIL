"""
2210 - 숫자판 점프
"""
grid = []
for i in range(5):
    data = list(map(int,input().split()))
    grid.append(data)

dr = [1,-1,0,0]
dc = [0,0,1,-1]
ret = set()
num = []
def dfs(pick,r,c):
    if pick == 6:## 숫자 6개 뽑기
        ret.add(tuple(num))
        return
    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0<= next_r < 5 and 0<= next_c <5:
            num.append(grid[next_r][next_c])
            dfs(pick+1, next_r, next_c)
            num.pop() # 백트랙킹

for i in range(5):
    for j in range(5):
        dfs(0,i,j)

print(len(ret))