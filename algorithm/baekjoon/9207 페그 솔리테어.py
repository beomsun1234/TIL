from sys import stdin
n = int(input())
input=stdin.readline
orgin_grid = []

grid = []

dr = [1,-1,0,0]
dc = [0,0,1,-1]


# '.'는 빈 칸, 'o'는 핀이 꽂혀있는 칸, '#'는 구멍이 없는

# 핀은 수평, 수직 방향으로 인접한 핀을 뛰어넘어서 그 핀의 다음 칸으로 이동하는 것만 허용된다.

## 처음시작 핀에서 종료핀까지 갈 수 있는 경우를 구한다.

def dfs(pin_cnt, move_cnt, grid):
    global mC
    global minCnt
   
    if pin_cnt < minCnt:
        mC = move_cnt
        minCnt = pin_cnt
    
    
    for i in range(5):
        for j in range(9):
            if grid[i][j] == "o":
                for d in range(4):
                    nr = i + (2*dr[d])
                    nc = j + (2*dc[d])
                    if 0<=nr<5 and 0<= nc <9:
                            # 전 칸이 핀일 경우만
                        npr = nr-dr[d]
                        npc = nc-dc[d]
                        if 0<=npr<5 and 0<=npc < 9:
                            if grid[npr][npc] == "o" and grid[nr][nc]=='.':
                                grid[i][j] = "."
                                grid[npr][npc] = "."
                                grid[nr][nc] = "o"
                                dfs(pin_cnt-1, move_cnt+1, grid)
                                grid[npr][npc] ="o"
                                grid[i][j] = "o"
                                grid[nr][nc] = "."
    
for i in range(n):
    grid = [list(input().rstrip()) for i in range(5)]
    p = 0
    for i in range(5):
        for j in range(9):
            if grid[i][j] == "o":
                p +=1
    minCnt = 10
    mC = 10
    input()
    dfs(p,0,grid)
    
    print(minCnt, mC)
