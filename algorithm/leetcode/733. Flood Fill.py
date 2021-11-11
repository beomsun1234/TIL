#733. Flood Fill   

"""""
    
    An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

    You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

    To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

    주의 consider the starting pixel



    input = image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
                        그리드               ,     시작포인트,    변경할 컬러


    output = [[2,2,2],[2,2,0],[2,0,1]] 다른컬로로 바꾼 그리드


    constraints

    m == image.length
    n == image[i].length
    1 <= m, n <= 50
    0 <= image[i][j], newColor < 216
    0 <= sr < m
    0 <= sc < n

    ds -> dfs 

    1. 처음 위치에 그리드 값을 저장해놓는다. -> var = grid[sr][sc]
    2.  주어진 시작위치를 기준으로  dfs를 실행한다.
    3. 4가지 방향으로 탐색을 진행 한다 [r, c] ( [1,0], [-1,0], [0,1], [0,-1])  
    4. 시작위치랑 값이 같다면 해당 위치 값을 newColor로 변경
    4. 그리드를 넘어가거나 시작위치 그리드 값이랑 같지 않을 경우 dfs 탐색 x
    5. 새로운 컬러값이 현재 컬러와 같은을 경우 dfs x 
"""

    # def dfs(image,r,c, nowColor):

    #     image[r][c]=2
    #     for i in range(4):
    #         nr = dr[i] + r
    #         nc = dc[i] + c
    #         if  0 <= nr < 3 and nc >= 0 and nc < 3  and image[nr][nc]==nowColor: 
    #             dfs(image,nr,nc, nowColor)


from typing import List


def dfs(image,r,c,nowColor):
    if  r<0  or r >= len(image) or  c<0 or  c >= len(image[1]):
        return
    if(image[r][c]!=nowColor):
        return
    image[r][c]=2
    for i in range(4):
        nr = dr[i] + r
        nc = dc[i] + c
        dfs(image,nr,nc, nowColor)


sr = 1 # x
sc  =1 # y

dr = [1,-1,0,0]
dc = [0,0,1,-1]


image = [[1,1,1],[1,1,0],[1,0,1]]

nowColor = image[sr][sc]

newColor = 2

if newColor != nowColor: 
    dfs(image,sr,sc,nowColor)

print(image)

### ---- leetcode 제출
class Solution:
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    
        dr = [1,-1,0,0]
        dc = [0,0,1,-1]
        
        n = len(image)
        m = len(image[0])
        nowColor = image[sr][sc]
            
        def dfs(image,r,c,nowColor,newColor):
            if  r<0  or r >= len(image) or  c<0 or  c >= len(image[1]):          
                return
            if(image[r][c]!=nowColor):
                return
                
            image[r][c]= newColor
            for i in range(4):
                nr = dr[i] + r
                nc = dc[i] + c
                dfs(image,nr,nc, nowColor, newColor)


        if newColor != nowColor: 
            dfs(image,sr,sc,nowColor,newColor)
            
        return image