"""
20056 마법상어와 파이어볼트

밑에는 실패한 처음 코드이다. 실패한 원인은 이동완료 후 grid처리에서 문제가 발생해서 실패했다..

import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
N,M,K = map(int,input().split())

grid = [[(0,0,0)]*(N+1) for _ in range(N+1)]
# r,c
## 0 = 위, 2 = 오른쪽,  4 하단, , 6 왼쪽
##  1 대각선 오른쪽 상단, 3 = 대각선 오른쪽 하단, 5 대각선 왼쪽 하단, 7 대각선 상단 왼쪽
dirs = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
q = deque()
for i in range(M):
    # ri, ci, mi, si, di
    data = list(map(int,input().split()))
    q.append(data)
def bfs():
    time = 0
    ret = 0
    while time < K:
        ret = 0
        time+=1
        # 파이어볼 저장
        tmp_fire_bolt = set()
        # 파이어볼 좌표 개수
        tmp_fire_bolt_cnt = defaultdict(list)
        tmp_fire_bolt_m_cnt = defaultdict(list)
        tmp_fire_bolt_s_cnt = defaultdict(list)
        tmp_fire_bolt_d = defaultdict(list)
        # ri, ci, mi, si, di
        # 파이어볼 이동
        while q:
            now_r, now_c , now_m, now_s, now_d = q.popleft()
            tmp_rr = now_r
            tmp_cc = now_c
            # 방향d로 s만큼이동
            next_r = now_r
            next_c = now_c
            for _ in range(now_s):
                next_r += dirs[now_d][0]
                next_c += dirs[now_d][1]
                #범위를 넘어가면 연결된 칸으로
                if next_r > N or next_r <=0:
                    if next_r > N:
                        next_r = 1
                    elif next_r <= 0:
                        next_r = N
                #범위를 넘어가면 연결된 칸으로
                if next_c > N or next_c <= 0:
                    if next_c > N:
                        next_c = 1
                    elif next_c <= 0:
                        next_c = N
            tmp_fire_bolt.add((next_r,next_c))
            # 다음칸 중복여부 체크
            if (next_r,next_c) in tmp_fire_bolt_cnt:
                tmp_fire_bolt_cnt[(next_r,next_c)] +=1
                tmp_fire_bolt_m_cnt[(next_r,next_c)]+=now_m 
                tmp_fire_bolt_s_cnt[(next_r,next_c)]+=now_s
                tmp_fire_bolt_d[(next_r,next_c)].append(now_d)
                #이동
                grid[next_r][next_c] = (-1,-1,-1)
                grid[tmp_rr][tmp_cc] = (0,0,0)
            else:
                tmp_fire_bolt_cnt[(next_r,next_c)] = 1
                tmp_fire_bolt_m_cnt[(next_r,next_c)] = now_m
                tmp_fire_bolt_s_cnt[(next_r,next_c)] = now_s
                tmp_fire_bolt_d[(next_r,next_c)] = [now_d]
                #이미 칸에 있다면
                if grid[next_r][next_c][0] >=1:
                    tmp_fire_bolt_cnt[(next_r,next_c)] +=1
                    tmp_fire_bolt_m_cnt[(next_r,next_c)]+= grid[next_r][next_c][0]
                    tmp_fire_bolt_s_cnt[(next_r,next_c)]+= grid[next_r][next_c][1]
                    tmp_fire_bolt_d[(next_r,next_c)].append(grid[next_r][next_c][2])
                    #이동
                    grid[next_r][next_c] = (-1,-1,-1)
                    grid[tmp_rr][tmp_cc] = (0,0,0)
                    continue
                #이동
                grid[next_r][next_c] = (now_m,now_s,now_d)
                grid[tmp_rr][tmp_cc] = (0,0,0)
        #이동이끝나면 2개이상 파이어볼이 있는 칸 검새
        for rr,cc in tmp_fire_bolt:
            if tmp_fire_bolt_cnt.get((rr,cc)) ==1:
                q.append((rr,cc,tmp_fire_bolt_m_cnt.get((rr,cc)),tmp_fire_bolt_s_cnt.get((rr,cc)), grid[rr][cc][2]))
                ret += tmp_fire_bolt_m_cnt.get((rr,cc))
            # 2개이상
            elif tmp_fire_bolt_cnt.get((rr,cc)) >=2:
                # d가 8이면 0,2,4,6
                # 9 1,3,5,7
                flag = set()
                for ddd in tmp_fire_bolt_d.get((rr,cc)):
                    num = ddd%2
                    flag.add(num)
                # 모두 짝수거나 홀수
                if len(flag) == 1:
                    tmp_m = tmp_fire_bolt_m_cnt.get((rr,cc)) // 5
                    tmp_s = tmp_fire_bolt_s_cnt.get((rr,cc)) // tmp_fire_bolt_cnt.get((rr,cc))
                    tmp_d = 0
                    if tmp_m == 0:
                        grid[rr][cc] = (0,0,0)
                        continue
                    for _ in range(4):
                        ret +=tmp_m
                        q.append((rr,cc,tmp_m,tmp_s,tmp_d))
                        tmp_d+=2
                else:
                    tmp_m = tmp_fire_bolt_m_cnt.get((rr,cc)) //5
                    tmp_s = tmp_fire_bolt_s_cnt.get((rr,cc)) //tmp_fire_bolt_cnt.get((rr,cc))
                    tmp_d = 1
                    if tmp_m == 0:
                        grid[rr][cc] = (0,0,0)
                        continue
                    for _ in range(4):
                        ret +=tmp_m
                        q.append((rr,cc,tmp_m,tmp_s,tmp_d))
                        tmp_d+=2
    
    return ret
print(bfs())
"""
from copy import deepcopy

N, M, K = map(int, input().split())
grid = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    if m != 0:
        # 상어의 질량이 0이 아니면 상어를 해당 위치에 놓는다.
        grid[r - 1][c - 1].append([m, s, d])

## 0 = 위, 2 = 오른쪽,  4 하단, , 6 왼쪽
##  1 대각선 오른쪽 상단, 3 = 대각선 오른쪽 하단, 5 대각선 왼쪽 하단, 7 대각선 상단 왼쪽
dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

for _ in range(K):
    tmp_grid = [[[] for _ in range(N)] for _ in range(N)]
    # 1. 모든 파이어볼이 이동한다.
    for y in range(N):
        for x in range(N):
            if grid[y][x] != []:
                for b in range(len(grid[y][x])):
                    nm, ns, nd = grid[y][x][b]
                    ny, nx = y + dirs[nd][0] * ns, x + dirs[nd][1] * ns
                    # 넘어 갈 경우 %를 통해 연결된 칸으로 보낸다.
                    nx = (nx + N) % N
                    ny = (ny + N) % N
                    tmp_grid[ny][nx].append([nm, ns, nd])
                    
    # 2. 2개 이상의 파이어볼이 있는 칸을 찾아 4개의 파이어볼을 만든다.
    for rr in range(N):
        for cc in range(N):
            if len(tmp_grid[rr][cc]) > 1:
                cm, cs, cd = 0, 0, []
                cnt = len(tmp_grid[rr][cc])
                for c in range(cnt):
                    cm += tmp_grid[rr][cc][c][0]
                    cs += tmp_grid[rr][cc][c][1]
                    cd.append(tmp_grid[rr][cc][c][2] % 2)
                cm = int(cm / 5)
                cs = int(cs / cnt)
                tmp_grid[rr][cc] = []
                if cm != 0: # 질량이 0 인 경우 소멸하는 조건 고려
                    if sum(cd) == 0 or sum(cd) == cnt: # 합쳐지는 파이어볼 방향이 모두 홀수거나 짝수인 경우
                        for i in range(4):
                            tmp_grid[rr][cc].append([cm, cs, i * 2])
                    else:
                        for j in range(4):
                            tmp_grid[rr][cc].append([cm, cs, j * 2 + 1])

    grid = deepcopy(tmp_grid)

# 남아있는 파이어볼 질량의 합 구하기
sum_m = 0
for y in range(N):
    for x in range(N):
        if grid[y][x] != []:
            for b in range(len(grid[y][x])):
                sum_m += grid[y][x][b][0]
print(sum_m)