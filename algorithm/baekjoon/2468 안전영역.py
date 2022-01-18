"""
백준 - 2468 안전영역

정말 간단하게 풀었다..하지만 메모리 초과에러 뿐만 아니라 재귀에러까지 발생했다.. sys.setrecursionlimit(10000) 최대 재귀 깊이를 설정하고
입력도 input=sys.stdin.readline 수정하니 메모리초과와 재귀에러는 해결됐다.. 여기서 90퍼대쯤에서 실패가 발했다.. for k in range(1,target+1): target만 큼만 돌면 됐는데 target+1만큼 돌아가니 실패한것 같다..

for k in range(target) 으로 변경해주니 통과했다.

"""

import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

# nxn
n = int(input())
#
grid = []
for i in range(n):
    grid.append(list(map(int,input().split())))
    

## 최대 높이값 받아오기
target = 0
for i in grid:
    for j in i:
       target = max(tmp,j) 

## 4방향
# 위 아래
dr = [1,-1,0,0]
# 왼, 오
dc = [0,0,-1,1]

def dfs(r,c,k):
    for i in range(4):
        next_r = r+dr[i]
        next_c = c+dc[i]
        if next_r <0 or next_r >= len(grid):
            continue
        if next_c <0 or next_c >= len(grid):
            continue
        if not visited[next_r][next_c] and grid[next_r][next_c] > k:
            visited[next_r][next_c] = True
            dfs(next_r,next_c,k)

cnt = 0
maxVal = 0
for k in range(target):
    cnt = 0
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] > k and not visited[i][j]:
                visited[i][j] = True
                dfs(i,j,k)
                cnt+=1
    maxVal = max(maxVal,cnt)
    

print(maxVal)