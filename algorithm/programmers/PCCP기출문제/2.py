from collections import deque

def solution(land):
    visited = [[False for _ in range(len(land[0]))] for _ in range(len(land))]



    dr = [1,-1,0,0]
    dc = [0,0,1,-1]

    def bfs(r,c):
        q = deque()
        q.append([r,c])
        visited[r][c] = True
        cnt = 1
        left = len(land[0])
        right = 0
        while q:
            rr, cc = q.popleft()
            for i in range(4):
                nr = rr + dr[i]
                nc = cc + dc[i]
                if land[rr][cc] == 1 and nc >= len(land[0]):
                    right = max(right, nc)
                if 0<= nr < len(land) and 0<= nc <len(land[0]):
                    if land[nr][nc] == 0: 
                        if i == 2:
                            right = max(right, nc)
                        elif i == 3:
                            left = min(left, nc)
                        continue
                    if visited[nr][nc]: continue
                    q.append([nr,nc])
                    cnt +=1
                    visited[nr][nc] = True


        if right == 0:
            right = len(land[0])
        if left == len(land[0]):
            left = -1
        return cnt, right, left

    section = []

    for i in range(len(land)):
        for j in range(len(land[0])):
            if not visited[i][j] and land[i][j] ==1:
                c,right,left = bfs(i,j)
                section.append([c,left,right])

    ans = 0
    a = [0] * len(land[0])
    for s in section:
        f = s[0]
        left = s[1]
        right = s[2]
        for i in range(left+1, right):
            a[i] += f

    a.sort()
    ans = a[-1]   
    answer = ans
    return answer
