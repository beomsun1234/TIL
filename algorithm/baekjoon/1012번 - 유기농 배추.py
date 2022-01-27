"""
1012번 - 유기농 배추

"""
def dfs(r,c):
        for i in range(4):
            next_r = r+dr[i]
            next_c = c+dc[i]
            if 0<=next_r< M and 0<=next_c<N and grid[next_r][next_c] == 1 and not visited[next_r][next_c]:
                visited[next_r][next_c] = True
                dfs(next_r,next_c)

dr = [1,-1,0,0]
dc = [0,0,1,-1]
t = int(input())
for _ in range(t):
    M, N, K = map(int,input().split())
    grid = [ [0]*N for row in range(M)]
    visited = [[False]*N for _ in range(M)]
    for i in range(K):
        r,c = map(int,input().split())
        grid[r][c] = 1
    cnt = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] ==1 and not visited[i][j]:
                cnt+=1
                visited[i][j] = True
                dfs(i,j)
            

    print(cnt)