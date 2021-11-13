"""
695. Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
OutPut: 6
Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is either 0 or 1.

DS - dfs

전역 변수로 Island의 포함된 땅 갯수를 카운트 하는 변수 선언
탐색 전 땅 갯수 카운트하는 변수 0으로 초기화
1. 주어진 그리드의 값이 1인 것을 찾아 탐색 
2. 1을 탐색하면 해당 그리드의 값을 2로 변경(방문 표시)
3. 땅 갯수 카운트 증가
3. 탐색 중 그리드 밖을 벗어나면 탐색 종료
4. 탐색 중 찾은 그리드의 값이 1이 아니면 탐색 종료
5. 탐색이 종료되면 이전 탐색된 아일랜드의 땅의 값과 현재 찾은 아일랜드의 땅의 값을 비교해서 큰 값을 저장

time = o(m*n)
"""

from typing import List


def dfs(grid, m,n):
    global ck
    if m < 0 or m >= len(grid) or n < 0 or n >= len(grid[0]):
        return
    if grid[m][n]!=1:
        return
    grid[m][n]=2
    ck+=1
    for i in range(4):
        nm = m+dm[i]
        nn = n+dn[i]
        dfs(grid,nm, nn)
#  [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid = [[0,0,0,0,0,0,0,0]]
dm = [1,-1,0,0]
dn = [0,0,-1,1]
ret = 0
global ck
for m in range (0,len(grid)):
    for n in range (0,len(grid[0])):
        if grid[m][n] == 1:
            ck = 0
            dfs(grid,m,n)
            ret = max(ret,ck)


print(ret)

## 제출 코드

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dm = [1,-1,0,0]
        dn = [0,0,-1,1]
        ret = 0
        global ck

        def dfs(grid, m, n):
            global ck
            if m < 0 or m >= len(grid) or n <0 or n >=len(grid[0]):
                return

            if grid[m][n] != 1:
                return
            grid[m][n] = 2
            ck+=1
            for i in range(4):
                nm = m + dm[i]
                nn = n + dn[i]
                dfs(grid,nm,nn)

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:
                    ck = 0
                    dfs(grid, m, n)
                    ret = max(ret,ck)


        return ret