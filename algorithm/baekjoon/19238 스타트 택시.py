from collections import deque

N, M, F = map(int,input().split())

city = []

for i in range(N):
    city.append(list(map(int,input().split())))


startR, startC = map(int,input().split())

startR -= 1
startC -= 1

customer = {}

for i in range(M):
    r,c,gr,gc = map(int,input().split())
    key = (r-1,c-1)
    customer[key] = [r-1,c-1,gr-1,gc-1,i]


dr = [-1,0,1,0]
dc = [0,-1,0,1]
finsh = [False] * M 

def checkOutBoundary(r,c):
    if 0<=r <N and 0<=c<N:
        return True 
    return False

def findCustomer(tr,tc):
    q = deque()
    q.append([tr,tc,0])
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    dist[tr][tc] = 0
    order = []
    mDis = float('inf')
    while q:
        rr, cc, d = q.popleft()
        key = (rr,cc)
        if d> mDis:
            break
        if key in customer:
            mDis = d
            order.append([d,rr,cc])

        for dir in range(4):
            nr = rr + dr[dir]
            nc = cc + dc[dir]
            if not checkOutBoundary(nr,nc):
                continue
            if city[nr][nc] != 0:
                continue
            if dist[nr][nc] == 0:
                continue
            if dist[nr][nc] == -1:   
                dist[nr][nc] = d+1
                q.append([nr,nc,d+1])
    if order:
        order.sort()
        return order[0][0], order[0][1], order[0][2] 
    return -1, -1, -1




def monvePath(r,c,gr,gc)->int:
    q = deque()
    q.append([r,c,0])
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    dist[r][c] = 0
    if r == gr and c == gc:
        return 0
    while q:
        rr, cc, d = q.popleft()
        if rr == gr and cc == gc:
            break
        for dir in range(4):
            nr = rr + dr[dir]
            nc = cc + dc[dir]
            if not checkOutBoundary(nr,nc):
                continue
            #길인 경우만
            if city[nr][nc] != 0:
                continue
            if dist[nr][nc] == 0:
                continue
            if dist[nr][nc] == -1:   
                dist[nr][nc] = d+1
                q.append([nr,nc,d+1])
    
    return dist[gr][gc]


order = []



for i in range(M):
    minUseF = 1000000000
    
    dis,r,c = findCustomer(startR, startC)
    if dis < 0:
        F = -1
        break
    # 목적지로 이동
    key = (r,c)
    #if key not in customer:
    #    F = -1
    #    break
    v = customer[key]
    del customer[key]
    useGF = monvePath(r, c, v[2], v[3])
    if useGF <0:
        F = -1
        break
    
    totalUseF = dis + useGF

    F -= totalUseF
    if F < 0:
        F = -1
        break
    F += (useGF *2)
    
    startR = v[2]
    startC = v[3]

print(F)
