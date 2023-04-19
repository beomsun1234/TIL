"""
l: 왼쪽으로 한 칸 이동
r: 오른쪽으로 한 칸 이동
u: 위쪽으로 한 칸 이동
d: 아래쪽으로 한 칸 이동
"""


import sys
sys.setrecursionlimit(10000)
dx = [1,0,0,-1]
dy = [0,-1,1,0]
dir = ['d','l', 'r', 'u']
aa = 0            
def dfs(nn, k, picks,n,m,x,y,r,c,ret):
    global aa
    # 현재 이동한거리가 k보다 클 경우 스탑
    if abs(x - r) + abs(y - c) + nn > k:
        return
    #정답을 찾았으면
    if aa == 1:
        return
    if nn == k:
        if x==r and y==c:
            d = ''
            aa= 1
            for i in picks:
                d += dir[i]
            ret.append(d)
        return
    
    for i in range(4):
        if 1 <= dx[i]+ x <= n and 1<=dy[i]+y <=m: 
            picks.append(i)
            dfs(nn+1,k, picks, n,m,dx[i]+ x,dy[i]+y,r,c,ret)
            picks.pop()
def solution(n, m, x, y, r, c, k):
    answer = ''
    picks = []
    ret = []
    #목적지까지 k만큼 이동 최단거리
    d = k - abs(x - r) + abs(y - c)
    # 0보다 작거나 같으면 이동불가, 탈출 지점에 도착하고 두번 이동하여 제자리로 돌아올수 있으므로 최단거리는 짝수가 되어야한다.
    if d <= 0 or d % 2 != 0:
        return 'impossible'
    dfs(0,k, picks,n,m,x,y,r,c,ret)
    
    if len(ret) == 0:
        answer = 'impossible'
    else:
        answer = ret[0]
    return answer
  
## 부분성공(시간초과코드)
"""
l: 왼쪽으로 한 칸 이동
r: 오른쪽으로 한 칸 이동
u: 위쪽으로 한 칸 이동
d: 아래쪽으로 한 칸 이동
"""

import sys
sys.setrecursionlimit(10000)
dir = ['d','l', 'r', 'u']
aa = 0
def searchMaze(n,m,x,y,r,c,picks):
    #m가로, n세로
    #r=y, c =x
    #move maze
    next_x = y
    next_y = x 
    for pick in picks:
        #0-l,1-r,2-u,3-d
        if pick == 0:
            next_x = next_x
            next_y = next_y +1
        if pick == 1:
            next_x = next_x -1
            next_y = next_y 
        elif pick == 2:
            next_x = next_x +1
            next_y = next_y 
        elif pick == 3:
            next_x = next_x
            next_y = next_y -1
        
        
        if 0>= next_y or next_y > n :
            return False
        if 0>= next_x or next_x> m:
            return False
    
    if next_x == c and next_y == r:
        return True

            
    return False       
            
def dfs(nn, k, picks,n,m,x,y,r,c,ret):
    global aa
    if aa == 1:
        return
    if nn == k:
        if searchMaze(n,m,x,y,r,c,picks):
            aa +=1
            d = ''
            for i in picks:
                d += dir[i]
            ret.append(d)
            return
        return
    for i in range(4):
        picks.append(i)
        dfs(nn+1,k, picks, n,m,x,y,r,c,ret)
        picks.pop()
def solution(n, m, x, y, r, c, k):
    answer = ''
    picks = []
    ret = []
    dfs(0,k, picks,n,m,x,y,r,c,ret)
    ret.sort()
    if len(ret) == 0:
        answer = 'impossible'
    else:
        answer = ret[0]
    return answer

