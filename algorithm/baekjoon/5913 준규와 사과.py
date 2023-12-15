r = 5
c = 5

k = int(input())

grid = [[0 for _ in range(c)] for _ in range(r)] 




for i in range(k):
    r,c = map(int,input().split())
    grid[r-1][c-1] = 1


dr = [-1,1,0,0]
dc = [0,0,1,-1]

J = [[0,0]]
H = [[4,4]]
visited = [[False for _ in range(5)] for _ in range(5)] 
visited[0][0] = True

answer = 0

def dfs(n): 
    global answer
    if J[-1][0] ==4 and J[-1][1] == 4:
        if len(J) == (25 - k):
            answer +=1
        return
    
    for i in range(4):
        njR = J[-1][0] + dr[i]
        njC = J[-1][1] + dc[i]
        
        if 0<=njR <5 and 0<= njC< 5:
            if grid[njR][njC] == 0 and not visited[njR][njC]:
                visited[njR][njC] = True
                J.append([njR,njC])
                dfs(n+1)
                J.pop()
                visited[njR][njC] = False

        



dfs(0)

print(answer)
