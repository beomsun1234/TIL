"""
17135 캐슬 디펜스

간단했지만 조금 시간이 걸린 문제이다.. 시간이 오래 걸린 부분은 삭제 할 수 있는 거리의 최솟값을 가지는 적이 2명 이상일 경우 가장 왼쪽에 있는거 제거하는 부분에서
시간이 조금 걸렸다. 나는 탐색을 하단 왼쪽 부터 탐색하기에 따로 처리 안해줘도 왼쪽부터 pos가 저장될 거라 생각했었다.. 여기서 잘 못 됐다.. 내 생각은 왼쪽이 우선일 거라 생각했는데
디버깅 해보니 위,아래가 왼쪽, 오른쪽보다 우선순위가 높았다.. 우선순위를 다시 왼쪽으로 잡아주니 통과할 수 있었다. 

로직은 이렇다. 우선 dfs를 사용해서 3명의 궁수 위치를 잡아준다. 잡아 준 이후 디펜스 게임을 시작한다. 공수가 공격을 시작한다. 궁수의 공격은
적이 정해진 공격 사정거리안에 들어온다면 map에 거리와, 좌표를 저장해주고, 해당 궁수와 적들의 거리를 측정하여 가장 가까운 거리의 값을 갱신해 나간다.
저장된 좌표와 거리 중 최단 거리의 값과 같은 값을 가지는 좌표만을 배열에 다시 넣어준다. 이때 최단거리를 가지는 적이 여러명일 경우 가장 왼쪽에 있는 적을 공격하기 위해서
해당 좌표에서 컬럼값이 가장 작은 값을 꺼내기 위해서 해당 좌표 배열을 컬럼 기준으로 오름차순 정렬해준다. 이 후 가장 앞에 좌표값을 제거할 적 좌표를 저장한 set에 저장해준다(중복으로 제거한 적을 처리하기 위해)
이 후 set의 길이는 제거한 적의 개수가 된다. 공격이 끝나면 적을 제거 한 후 모든 적을 한칸 내려준다. 게임이 끝나면 죽인 적의 개수가 최대값이라면 최대값을 갱신해 나가며 사용한 값들을 초기화 시켜준다.
"""


import copy
from collections import defaultdict
N,M, D = map(int,input().split())

grid = []
for i in range(N):
    data = list(map(int,input().split()))
    grid.append(data)

combi = []
global hit 
t_grid = copy.deepcopy(grid)
hit = 0
global answer
answer = 0

# 모든 적이 격자판에서 제외되면 게임 끝
def check_enemy():
    for i in range(N):
        for j in range(M):
            if grid[i][j] ==1:
                return False
    return True

# 궁수 위치를 받고 게임 시작
def start_game(a_combi):
    global hit 
    archer_pos_coloum = []
    for idx in a_combi:
        archer_pos_coloum.append(idx)
    #idx는 적들이 있는 grid 컬럼
    while not check_enemy():
        attacked_enemy_pos = archer_attack(archer_pos_coloum)
        enemy_move(attacked_enemy_pos)
    return hit

# 궁수 공격
def archer_attack(a_pos_c):
    global hit 
    #궁수 포지션 배치
    a_r = N
    cnt= 0
    enemy_dist_tmp = [100000] * M
    enemy_kil_pos_tmp = defaultdict(list)
    enemy_kil_pos = set()
    #밑에 부터시작
    for i in range(N-1,-1,-1):
        for j in range(M):
            #만약 적이면
            if grid[i][j] == 1:
                #거리 확인
                for k in a_pos_c:
                    dist = abs(i-a_r) + abs(j-k)
                    # D 이하이면 추가
                    if dist <= D:
                        if enemy_dist_tmp[k] > dist:
                            enemy_dist_tmp[k] = dist
                        if not enemy_kil_pos_tmp[k]:
                            enemy_kil_pos_tmp[k] = [[dist,i,j]]
                        else:
                            enemy_kil_pos_tmp[k].append([dist,i,j])
    # 추가된 적 공격가능 정보를 바탕으로 최소값인 경우 제거
    for i in a_pos_c:
        if not enemy_kil_pos_tmp.get(i):
            continue
        tt = []
        for j in enemy_kil_pos_tmp.get(i):
            #최솟값을 가지는 적 거리 저장
            if j[0] == enemy_dist_tmp[i]:
                tt.append((j[1],j[2]))
        # 만약 최솟값을 가지는 적이 2명 이상일 경우 가장 왼쪽에 있는거 제거하기위해 col이 작은 값 선택
        if len(tt) >= 2:
            tt.sort(key=lambda x:x[1])
        # 삭제 조건에 맞는 pos저장(set)
        enemy_kil_pos.add((tt[0][0], tt[0][1]))
    # 중복해서 제거할 수 있으므로 set을 통해 몇개 제거 됐는지 체크
    hit += len(enemy_kil_pos)
    return enemy_kil_pos

# 공격 종료 후 적 이동
def enemy_move(enemy_kil_pos):
    if enemy_kil_pos:
        for r,c in enemy_kil_pos:
            grid[r][c] = 0
    grid_tmp = copy.deepcopy(grid)
    # 적 옯기기
    for rr in range(1,N):
        for cc in range(M):
            grid[rr][cc] = grid_tmp[rr-1][cc]
    for i in range(M):
        grid[0][i] = 0
    
# 궁수의 위치를 랜덤으로 3개 뽑는다. 조합사용(중복 x)
def dfs(pick,idx):
    global hit
    global answer
    if pick == 3:
        answer = max(answer,start_game(combi))
        # 초기화
        hit = 0
        for i in range(N):
            for j in range(M):
                grid[i][j] = t_grid[i][j]
        return
    for i in range(idx,M):
        combi.append(i)
        dfs(pick+1, i+1)
        combi.pop()

dfs(0,0)

print(answer)