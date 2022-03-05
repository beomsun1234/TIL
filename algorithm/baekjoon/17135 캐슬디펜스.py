"""
17135 캐슬 디펜스
성공 x
"""

import copy
N,M, D = map(int,input().split())

grid = []


for i in range(N):
    data = list(map(int,input().split()))
    grid.append(data)

combi = []
global hit 
hit = 0
global answer
answer = 0
def check_enemy():
    for i in range(N):
        for j in range(M):
            if grid[i][j] ==1:
                return False

    return True

def turn_game(a_combi):
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
    enemy_move_pos = set()
    for i in range(N):
        for j in range(M):
            # 3번 쏘면
            if cnt == 3:
                break
            #만약 적이면
            elif grid[i][j] == 1:
                #거리 확인
                for k in a_pos_c:
                    dist = abs(i-a_r) + abs(j-k)
                    if dist == D:
                        cnt+=1
                        enemy_move_pos.add((i,j))
    hit += len(enemy_move_pos)
    return enemy_move_pos
def enemy_move(enemy_move_pos):
    for r,c in enemy_move_pos:
        grid[r][c] = 0
    grid_tmp = copy.deepcopy(grid)
    for i in range(1,N):
        for j in range(M):
            grid[i][j] = grid_tmp[i-1][j] 
            grid_tmp[i][j] = grid[i][j]
    # 내리고난후 맨위는 0으로 초기화
    for i in range(M):
        grid[0][i] = 0

# 궁수의 위치를 랜덤으로 3개 뽑는다. 조합사용(중복 x)
def dfs(pick,idx):
    global hit
    global answer
    if pick == 3:
        t_grid = copy.deepcopy(grid)
        answer = max(answer,turn_game(combi))
        hit = 0
        # 초기화
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