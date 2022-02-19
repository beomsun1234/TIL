"""
20208 - 진우의 민트초코
dfs를 사용해서 방문할 민트초코 좌표들의 순열을 구한다(뽑는 순서도 중요하기에 순열로). 여기 까지는 간단하게 접근 할 수 있다.
이제 뽑은 순열을 가지고 거리를 구해서 갈 수 있는곳인지 확인해야한다. 여기서 어떻게 이동해야할지 감이 잡히지 않았다.. 다른 분의 풀이를 보니
거리구하기 공식을 이용 현재 좌표에서 다음 좌표까지의 거리를 구하면 됐었다... 
아래를 보면(2= 민트초고, 1은 처음 위치(처음시작 위치는 홈)) 순열이 (0,0) , (2,2)가 나왔다고 가정하자

2 0 2
0 1 0

step 1(집에서 시작)

현재 위치(1,1)에서 처음 민트(0,0까지의 거리는  |dist = abs(now_r - now_mint_r) +  abs(now_c - now_mint_c)는 2이다.
여기서 이제 거리당 1의 hp가 소모되므로 현재 hp와 거리를 비교하여 갈 수 있는지 없는지 체크하고 갈 수 없다면 탐색을 종료한다.
갈 수 있다면 체력을 조건에 따라 감소 증가시키고 카운트를 증가시킨다. 이후 현재 체력으로 집으로 돌아 갈 수 있다면 현재 카운트를 max값과 비교하여 max를 갱신한다.
체크 후 다음 민트를 찾으러가기 위해 현재 위치를 방문한 민트의 좌표로 바꿔준다.


"""

N, M, H = map(int, input().split())
grid = []
global answer
answer = 0
for i in range(N):
    data = list(map(int,input().split()))
    grid.append(data)
    
home_pos = []
mint_pos = []
mint_cnt = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            mint_pos.append([i,j])
            mint_cnt+=1
        if grid[i][j] == 1:
            home_pos.append([i,j])

visited = [False] * mint_cnt


mint_combi = []

## 민트초고에 대한 순열 구하기
def dfs(pick):
    if pick == mint_cnt:
        move(mint_combi)
        return
    for i in range(mint_cnt):
        if not visited[i]:
            visited[i] = True
            mint_combi.append(i)
            dfs(pick+1)
            visited[i] = False
            mint_combi.pop()

def move(combi):
    global answer
    now_r = home_pos[0][0]
    now_c = home_pos[0][1]
    tmp_m = M
    cnt = 0
    for i in combi:
        mint_r = mint_pos[i][0]
        mint_c = mint_pos[i][1]
        dist = abs(now_r- mint_r) + abs(now_c - mint_c)
        if dist > tmp_m: #거리가 멀다면 못간다.
            return
        # 갈 수 있다면 현재 체력을 이동한 만큼 빼고
        tmp_m -= dist
        # 민트초고를 먹었으니 현재 체력 증가
        tmp_m +=H
        # 카운트 증가
        cnt+=1
        # 현재 민트 집까지 돌아갈수있는지 
        tohome = abs(home_pos[0][0] - mint_r) + abs(home_pos[0][1] - mint_c)
        # 현재 채력으로 집가지 갈 수 있다면
        if tohome <= tmp_m:
            answer = max(answer,cnt)
        # 다음 시작위치를 현재 민트로
        now_r = mint_r
        now_c = mint_c

dfs(0)
print(answer)