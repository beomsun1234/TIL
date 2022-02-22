"""
15683 감시

간단했다. 코드가 지저분하지만 주어진대로 구현하면 되는 문제였다. 

로직은 간단하다 5개의 cctv가 존재하고 각 시시티비 번호마다 감시 방향이 다르고 각 cctv는 90도 방향으로 회전 할 수 있다.
5번 시시티비는 회전해도 항상 같으므로 1~4 번까지의 cctv를 4가지 방향으로 회전 할 수 있으므로 5번을 제외한 cctv개수만큼 중복 순열을 구해준다.
순열의 값이 0인 경우 오른쪽(회전), 1인 경우 아래, 2인 경우 왼쪽 , 3인경우 위쪽으로 정하고 얻은 순열을 바탕으로 cctv를 회전하여 
사각지대의 수가 가장 적은 값을 리턴하면 된다.

여기서 주의 할 점은 본인은 내자마자 바로 틀렸는데 원인은 왼쪽 방향이랑, 위쪽방향일 경우 벽처리에서 잘 못 생각하여 실패하였다..
실패코드는

왼쪽일 경우
r , c = cctv_spin_pos[i]
for j in range(0,c):
    if grid[r][j] == 6:
        break
    tmp[r][j] = -1

이부분에서 현재 위치에서 시작해서 왼쪽으로 가면서 감시가능 표시를해야하는데 현재코드에서는 감시가능 표시(-1)를 그리드상의 끝에서 시작 함으로 
실패한다. 당연했다.. 현재 주어진 테스트 케이스는 통과하나

7 5
0 6 6 6 6
6 0 6 4 6
6 6 1 2 6
6 0 1 6 0
6 6 0 0 6
0 6 0 6 6
3 0 6 0 0

해당 케이스는 실패했다.. 위 문제를 아래와 같이 수정해 주니 통과할 수 있었다.

r , c = cctv_spin_pos[i]
for j in range(c,-1,-1):
    if grid[r][j] == 6:
        break
    tmp[r][j] = -1

"""

# 전부 4방향이라 생각하고 하자 
import copy
N,M = map(int, input().split())
grid = []
for i in range(N):
    data = list(map(int,input().split()))
    grid.append(data)

# 5번시시티비 제외
combi_cnt = 0
cctv_spin_pos = []
cctv_cnt = 0
cctv_five_pos = []
global min_val
min_val = N*M
for i in range(N):
    for j in range(M):
        if 0<grid[i][j] <5:
            combi_cnt+=1
            cctv_spin_pos.append((i,j,grid[i][j]))
            cctv_cnt+=1
        if grid[i][j] == 5:
            cctv_cnt +=1
            cctv_five_pos.append((i,j))

cctv_spin_combi = []

def spin(cctv_spin_combi):
    tmp = copy.deepcopy(grid)
    # 5번 시시티비 박기
    if len(cctv_five_pos) >0:
        for five_r,five_c in cctv_five_pos:
            for j in range(five_c+1,M):
                if grid[five_r][j] == 6:
                    break
                tmp[five_r][j] = -1
            for j in range(five_r+1,N):
                if grid[j][five_c] == 6:
                    break
                tmp[j][five_c] = -1
            for j in range(five_c,-1,-1):
                if grid[five_r][j] ==6:
                    break
                tmp[five_r][j] = -1
            for j in range(five_r,-1, -1):
                if grid[j][five_c] == 6:
                    break
                tmp[j][five_c] = -1
    for i in range(combi_cnt):
        r,c, cctv_num = cctv_spin_pos[i]
        if cctv_num == 1:
            # 0 -> 오른 
            if cctv_spin_combi[i] == 0:
                for j in range(c+1,M):
                    if grid[r][j]==6:
                        break
                    tmp[r][j] = -1
            # 1  아래
            elif cctv_spin_combi[i] == 1:
                for j in range(r+1,N):
                    if grid[j][c] == 6:
                        break
                    tmp[j][c] = -1
            # 2  <-, 왼쪽
            elif cctv_spin_combi[i] == 2:
                #왼
                for j in range(c,-1,-1):
                    if grid[r][j] ==6:
                        break
                    tmp[r][j] = -1
            # 3 위
            elif cctv_spin_combi[i] == 3:
                for j in range(r,-1, -1):
                    if grid[j][c] == 6:
                        break
                    tmp[j][c] = -1
        elif cctv_num == 2:
            # 왼,오
            if cctv_spin_combi[i] == 0 or cctv_spin_combi[i] == 2:
                for j in range(c+1,M):
                    if grid[r][j] ==6:
                        break
                    tmp[r][j] = -1
                #왼
                for j in range(c,-1,-1):
                    if grid[r][j] ==6:
                        break
                    tmp[r][j] = -1
            # 위,아래
            elif cctv_spin_combi[i] == 1 or  cctv_spin_combi[i] == 3:
                for j in range(r,-1, -1):
                    if grid[j][c] == 6:
                        break
                    tmp[j][c] = -1
                for j in range(r,N):
                    if grid[j][c] ==6:
                        break
                    tmp[j][c] = -1
        
        elif cctv_num == 3:
            # 0 위,오
            if cctv_spin_combi[i] == 0:
                #위
                for j in range(r,-1, -1):
                    if grid[j][c] == 6:
                        break
                    tmp[j][c] = -1
                #오
                for j in range(c+1,M):
                    if grid[r][j] ==6:
                        break
                    tmp[r][j] = -1

            # 1 오,아래
            elif cctv_spin_combi[i] == 1:
                #오
                for j in range(c+1,M):
                    if grid[r][j] ==6:
                        break
                    tmp[r][j] = -1
                #아래
                for j in range(r,N):
                    if grid[j][c] ==6:
                        break
                    tmp[j][c] = -1
            # 2 아래,왼
            elif cctv_spin_combi[i] == 2:
                #아래
                for j in range(r,N):
                    if grid[j][c] ==6:
                        break
                    tmp[j][c] = -1
                #왼
                for j in range(c,-1,-1):
                    if grid[r][j] ==6:
                        break
                    tmp[r][j] = -1
            # 3 왼,위 문제발생
            elif cctv_spin_combi[i] == 3:
                #왼
                for j in range(c,-1,-1):
                    if grid[r][j] ==6:
                        break
                    tmp[r][j] = -1
                # 위
                for j in range(r,-1, -1):
                    if grid[j][c] == 6:
                        break
                    tmp[j][c] = -1

        elif cctv_num == 4:
            # 왼,위,오
            if cctv_spin_combi[i] == 0:
                #왼
                for j in range(c,-1,-1):
                    if grid[r][j] ==6:
                        break
                    tmp[r][j] = -1
                #위
                for j in range(r,-1, -1):
                    if grid[j][c] == 6:
                        break
                    tmp[j][c] = -1
                #오른
                for j in range(c+1,M):
                    if grid[r][j] ==6:
                        break
                    tmp[r][j] = -1

            # 1 위,오,아래
            elif cctv_spin_combi[i] == 1:
                #위
                for j in range(r,-1, -1):
                    if grid[j][c] == 6:
                        break
                    tmp[j][c] = -1
                #오른
                for j in range(c+1,M):
                    if grid[r][j] ==6:
                        break
                    tmp[r][j] = -1
                #아래
                for j in range(r+1,N):
                    if grid[j][c] ==6:
                        break
                    tmp[j][c] = -1
            # 2 왼,아래,오른
            elif cctv_spin_combi[i] == 2:
                #아래
                for j in range(r+1,N):
                    if grid[j][c] ==6:
                        break
                    tmp[j][c] = -1
                #오른
                for j in range(c+1,M):
                    if grid[r][j] ==6:
                        break
                    tmp[r][j] = -1
                #왼
                for j in range(c,-1,-1):
                    if grid[r][j] ==6:
                        break
                    tmp[r][j] = -1

            # 3 아래,왼,위
            elif cctv_spin_combi[i] == 3:
                #아래
                for j in range(r+1,N):
                    if grid[j][c] ==6:
                        break
                    tmp[j][c] = -1
                #왼
                for j in range(c,-1,-1):
                    if grid[r][j] ==6:
                        break
                    tmp[r][j] = -1
                #위
                for j in range(r,-1, -1):
                    if grid[j][c] == 6:
                        break
                    tmp[j][c] = -1
    cal_min(tmp)

def cal_min(tmp_grid):
    global min_val
    val = 0
    for i in range(N):
        for j in range(M):
            if tmp_grid[i][j] == 0:
                val+=1
    min_val = min(min_val, val)

# 회전 조합
def dfs(pick):
    if pick == combi_cnt:
        # 0 ->, 1  아래 , 2  <-, 3 위
        spin(cctv_spin_combi)
        return
    # 4방향으로 회전가능
    for i in range(4):
        cctv_spin_combi.append(i)
        dfs(pick+1)
        cctv_spin_combi.pop()

dfs(0)
print(min_val)