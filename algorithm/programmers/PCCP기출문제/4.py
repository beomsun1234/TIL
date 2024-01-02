# 4.py

def solution(maze):
    R = len(maze)
    C = len(maze[0])
    
    red = []
    redG = []
    blue = []
    blueG = []
    visitiedR = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    visitiedB = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 1:
                maze[i][j] = 0
                red.append([i,j])
                visitiedR[i][j] = True
            elif maze[i][j] == 2:
                maze[i][j] = 0
                visitiedB[i][j] = True
                blue.append([i,j])
            elif maze[i][j] == 3:
                redG.append([i,j])
            elif maze[i][j] == 4:
                blueG.append([i,j])
    dr = [1,-1,0,0]
    dc = [0,0, 1,-1]
    global check
    check = False
    global ans
    ans = 1000000
    def dfs(n):
        global check
        global ans
        if ans < n//2:
            return
        if n > 1:
            # 2번움직임
            if n % 2 != 0:
                if red[-1][0] == redG[-1][0] and red[-1][1] == redG[-1][1]:
                    if not (blueG[-1][0] == blue[-1][0] and blueG[-1][1] == blue[-1][1]):
                        dfs(n+1)
            elif n % 2 ==0:
                if (blueG[-1][0] == blue[-1][0] and blueG[-1][1] == blue[-1][1]):
                    if not (red[-1][0] == redG[-1][0] and red[-1][1] == redG[-1][1]):
                        print("red=", red)      
                        print("blue=", blue)  
                        dfs(n+1)
            if red[-1][0] == redG[-1][0] and red[-1][1] == redG[-1][1] and blueG[-1][0] == blue[-1][0] and blueG[-1][1] == blue[-1][1]:
                
                ans = min(ans,n//2)
                check = True
                return
        for i in range(4):
            if n % 2 ==0:
                r = blue[-1][0]
                c = blue[-1][1]
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<len(maze) and 0<=nc<len(maze[0]):
                    if red[-1][0] == nr and red[-1][1] == nc:
                        if not (red[-1][0] == redG[-1][0] and red[-1][1] == redG[-1][1]):
                            continue 
                    if visitiedB[nr][nc]:
                        continue
                    if maze[nr][nc] != 5 :
                        if nr == blueG[-1][0] and nc== blueG[-1][1]:
                            visitiedB[nr][nc] = True
                            tmp = maze[nr][nc] 
                            maze[nr][nc] = 5
                            blue.append([nr,nc])
                            dfs(n+1)
                            blue.pop()
                            visitiedB[nr][nc] = False
                            maze[nr][nc] = tmp
                        else:
                            visitiedB[nr][nc] = True
                            blue.append([nr,nc])
                            dfs(n+1)
                            blue.pop()
                            visitiedB[nr][nc] = False
                
            else:
                r = red[-1][0]
                c = red[-1][1]
                nr = r+ dr[i]
                nc = c + dc[i]
                if 0<=nr<len(maze) and 0<=nc<len(maze[0]):
                    if blue[-1][0] == nr and blue[-1][1] == nc:
                        if not (blue[-1][0] == blueG[-1][0] and blue[-1][1] == blueG[-1][1]):
                            continue 
                    if visitiedR[nr][nc]:
                        continue
                    if maze[nr][nc] != 5:
                        if nr == redG[-1][0] and nc== redG[-1][1]:
                            visitiedR[nr][nc] = True
                            red.append([nr,nc])
                            tmp = maze[nr][nc]
                            maze[nr][nc] = 5
                            dfs(n+1)
                            red.pop()
                            maze[nr][nc] = tmp
                            visitiedR[nr][nc] = False
                        else:
                            visitiedR[nr][nc] = True
                            red.append([nr,nc])
                            dfs(n+1)
                            red.pop()
                            visitiedR[nr][nc] = False


    dfs(1)
    if check == False or ans == 0:
        answer = 0
    else:
        answer = ans
    

    return answer
