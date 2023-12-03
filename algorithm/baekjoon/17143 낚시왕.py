R, C, M = map(int,input().split())

global shark_weight
shark_weight = 0

global shark_db
shark_db = {}


# r,c, s, d,z =크기

for i in range(M):
    r,c,s,d,z = map(int,input().split())
    key = (r,c, 0)
    # 하나의 칸에 둘이상 존재하지 않는다.
    shark_db[key] = [r,c,s,d,z]

def catchShark(man_c, time):
    global shark_weight
    for r in range(1,R+1):
        key = (r,man_c, time)
        if key not in shark_db:
            continue
        # 땅(r) 과 가장 가까이 있는 상어 하나만 잡는다.
        shark = shark_db[key]

        shark_weight += shark[4]
        shark_db.pop(key,None)
        break
    return

#상,하,우,좌
dr = [0,-1,1,0,0]
dc = [0,0,0,1,-1]



def trunDir(d):
    if d == 1:
        return 2
    if d == 2:
        return 1
    if d == 3:
        return 4
    if d == 4:
        return 3

def move(r,c,s,d,z, time):
    global shark_db
    nr = r
    nc = c
    nd = d
    ns = s
    while ns>0:
        ns-=1
        nr = nr + dr[nd]
        nc = nc + dc[nd]
        if 0<nr<=R and 0< nc <= C:
            continue
        else:
            nd = trunDir(nd) 
            nr = nr + dr[nd]
            nc = nc + dc[nd]
            ns+=1
    key = (nr,nc, time)
    
    if key not in shark_db:
        shark_db[key] = [nr,nc,s,nd,z]
        return 
    shark = shark_db[key]
    if shark[4] >= z:
        return
    
    shark_db.pop(key,None)
    shark_db[key] = [nr,nc,s,nd,z]
    return 



# 같은 칸일 경우 덩치가 가장 큰 상어가 전부를 잡아먹는다.
def moveShark(time):
    global shark_db
    for r in range(1,R+1):
        for c in range(1, C+1):
            key = (r,c, time)
            if key not in shark_db:
                continue
            # 상어가 있따면 이동
            shark = shark_db[key]
            nTime = time +1 
            move(r,c, shark[2],  shark[3], shark[4], nTime)
    return

time = 0

for man_c in range(1,C+1):
    
    catchShark(man_c=man_c, time= time)
    moveShark(time=time)
    time +=1
    

print(shark_weight)
