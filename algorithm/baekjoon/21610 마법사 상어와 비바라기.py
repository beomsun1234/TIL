"""
21610 마법사 상어와 비바라기

간단했다. 구름 이동을 M번 명령하면 5가지 순서대로 진행되며 모든 명령이 종류된 후 바구니에 들어있는 물의 양을 구하면 된다.

구름 이동을 deque를 이용하여 구현하였다. deque를 사용한 이유는 각 명령마다 여려개의 좌표가 이동하기에 각좌표를 큐에 집어넣고 각 좌표의 이동이 완료되면 다음 명령을 진행한다.
(N, 1), (N, 2), (N-1, 1), (N-1, 2)를 시작점으로 명령에 따라 이동을 구현하고 나머지 명령을 순서대로 진행하면 답을 도출 할 수 있다.



"""


from collections import deque

N,M = map(int,input().split())

#  8개의 방향이 있다 
## 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
grid = []
for i in range(N):
    data = list(map(int,input().split()))
    grid.append(data)
dd = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
dir = []
for i in range(M):
    data = list(map(int,input().split()))
    dir.append((data[0], data[1]))

q = deque([(N-1,0),(N-1,1),(N-2,0),(N-2,1)])
cnt = 0

# 2구름이 있는  칸 바구니물의 양증가 함수
def update_basket(tmp):
    for r,c in tmp:
        grid[r][c] +=1
        

# 4물복사 버그
def water_copy_bug_magic(tmp):
    for r,c in tmp:
        cnt = 0
        for i in range(1,len(dd),2):
            nr = r+dd[i][0]
            nc = c+dd[i][1]
            if 0<=nr<N and 0<=nc<N:
                if grid[nr][nc] > 0:
                    cnt +=1
        grid[r][c] += cnt
    
# 5바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
def make_cloud(tmp):
    cloud = []
    for i in range(N):
        for j in range(N):
            if (i,j) not in tmp and grid[i][j] >=2:
                grid[i][j] -=2
                cloud.append((i,j))
    return cloud
while cnt < M:
    # 1구름이동
    tmp = []
    while q:
        rr, cc = q.popleft()
        for i in range(dir[cnt][1]):
            rr += dd[dir[cnt][0]-1][0]
            cc += dd[dir[cnt][0]-1][1]
            if rr < 0:
                rr = N + rr 
            elif rr>=N:
                rr = rr - N
            if cc < 0 :
                cc = N + cc 
            elif cc>=N:
                cc = cc - N
        tmp.append((rr,cc))
    
    # 구름이 있는 칸의 바구니 물 1 증가
    update_basket(tmp)
    water_copy_bug_magic(tmp)
    q = deque(make_cloud(tmp))
    cnt +=1
answer = 0
for i in grid:
    answer+=sum(i)
print(answer)