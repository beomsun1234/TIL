"""

"""

R,C = map(int, input().split())

trees = []
for i in range(R):
    val = list(map(int, input().split()))
    trees.append(val)

# 0 - ㄱ, 1 - ㄴ(반대), 2- ㄴ , 3 -  ㄱ(반대)
dr = [  0, -1, -1, 0]
dc = [ -1,  0,  0, 1]
dr2 = [ 1,  0,  0, 1]
dc2 = [ 0, -1,  1, 0]

visited = [[False for _ in range(C)] for _ in range(R)]

ret = 0
pick = []
def dfs(r,c,n,t):
    global ret

    if R <= 1 or C <=1:
        return
    if c == C:
        c =0
        r +=1
    if r == R :
        ret = max(ret, t)
        return
    
    if not visited[r][c]: 
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            nr2 = r + dr2[d]
            nc2 = c + dc2[d]
            if 0<= nr <R and 0<= nc <C and 0<= nr2 < R and 0<= nc2 <C:
                if visited[nr][nc] or visited[nr2][nc2] or visited[r][c]:
                    continue
                visited[r][c] = True
                visited[nr][nc] = True
                visited[nr2][nc2] = True
                tmp = 0
                tmp = trees[r][c] *2
                tmp += trees[nr][nc] 
                tmp +=trees[nr2][nc2]
                dfs(r,c+1,n+1,tmp+t)
                visited[r][c] = False
                visited[nr][nc] = False 
                visited[nr2][nc2] = False
    dfs(r,c+1,n+1,t)

dfs(0,0,0,0)

print(ret)
