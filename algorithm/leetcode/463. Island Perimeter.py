"""
463. Island Perimeter

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Constraints:
        row == grid.length
        col == grid[i].length
        1 <= row, col <= 100
        grid[i][j] is 0 or 1.

DS - dfs

1. dfs로 땅을 찾는다(lake가 아니고 땅으로 연결된 곳)
- 땅 하나당 4개의 스트립을 가짐 -> 땅과 땅이 연결되어있을 경우 겹치는 부분이 제거되어 8개가 아닌 6개를 가진다. 
- 땅 주변에 물이 있으면 확정적으로 스트립을 가짐 주변에 아무것도 연결 할 수 없기 때문에 잃는 것이 없음
2. 찾은 곳이 땅일 경우 주변에 물이 있는지 확인 한다.
3. 물이 있으면 카운트를 증가해 준다.(스트립 개수)

edge case = [[1]]
- 처음 땅을 찾고 주변에 아무것도 없을 경우 이다. 즉 땅이 1면 4개의 스트립을 가져야하기에 
dfs 중 그리드에서 벋어 날 경우 count를 증가해준다. 찾는 위치가 그리드의 밖이여도 확정적으로 스트립을 가진다.


time = o(m*n) -> 우선 n*n의 그리드(직사각형)에서 값이 1인 것을 찾기 때문이다.
"""

from typing import List


def dfs(grid, cr,cc, val):
    global ck, count
    ## 그리드 끝
    if cr < 0 or cr >= r or cc <0 or cc>=c:
        ck+=1
        return 
    if grid[cr][cc] != val:  
        return
    ## 내 위치가 땅일 때 주변 탐색
    if cr != 0:
        if (grid[cr-1][cc]) == 0:
            ck +=1
    if cr != r-1:
        if grid[cr+1][cc] == 0:
            ck +=1
    if cc != 0:
        if grid[cr][cc-1] == 0:
            ck +=1
    if cc != c-1:
        if grid[cr][cc+1] == 0:
            ck+=1
    grid[cr][cc] = 2
    for i in range(4):
        nr = dr[i] + cr
        nc = dc[i] + cc
        dfs(grid,nr,nc,val)
##  [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]] , [[1,1],[1,1]]
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
global ck
ck = 0
# 1= rand -> 0은 lake
dr = [1,-1,0,0]
dc = [0,0,-1,1]

r = len(grid)
c = len(grid[0])

for i in range(r):
    for j in range(c):
        if grid[i][j]==1:
            dfs(grid,i,j,1)
            break

print(ck)
print("결과=",ck)

## 제출 코드
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dr = [1,-1,0,0]
        dc = [0,0,-1,1]

        r = len(grid)
        c = len(grid[0])
        global ck
        ck = 0

        def dfs(grid, cr,cc, val):
            global ck
            if cr < 0 or cr >= r or cc <0 or cc>=c:
                ck+=1
                return
            if grid[cr][cc] != val:
                return
            if cr != 0:
                if (grid[cr-1][cc]) == 0:
                    ck +=1
            if cr != r-1:
                if grid[cr+1][cc] == 0:
                    ck +=1
            if cc != 0:
                if grid[cr][cc-1] == 0:
                    ck +=1
            if cc != c-1:
                if grid[cr][cc+1] == 0:
                    ck+=1

            grid[cr][cc] = 2
            for i in range(4):
                nr = dr[i] + cr
                nc = dc[i] + cc
                dfs(grid,nr,nc, val)

        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    dfs(grid,i,j,1)

        return ck