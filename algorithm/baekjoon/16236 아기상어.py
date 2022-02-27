"""
아기 상어

좌표거리로 계산하면 안된다.. 나는 상어의 크기를 기준으로 좌표거리를 계산하니 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없지만 
좌표 계산으로 하면 지나갈 수 있게된다.. 열심히 코드를 작성하다 예제 4번에서 답이 달라서 답을 따라가 보다가 오류를 발견했고 문제를 다시 읽었다..
예를 들어 아래의 경우(인덱스 0 부터시작) 상어 위치는 (5,1) 현재 크기가 2일 경우 갈 수 있는 곳은 1 번 물고기가 있는
(5,5), (0,5) 가장 가까운 거리는 6이지만 좌표계사느로 할 경우 4가된다.. (abs(shark_pos_r-i) + abs(shark_pos_c -j) )

6
6 0 6 0 6 1
0 0 0 0 0 2
2 3 4 5 6 6
0 0 0 0 0 2
0 2 0 0 0 0
3 9 3 0 0 1

아래 코드는 위에서 설명한 좌표거리를 계산한 실패한 로직이다.

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue  
            if 0< grid[i][j] < weight:
                visited[i][j] = True
                dist =  abs(shark_pos_r-i) + abs(shark_pos_c -j) 
                min_dist = min(min_dist, dist)
                tmp_fish_pos.append((dist,i,j))

좌표 계산 대신 현재 상어 무게에서 상어가 갈 수 있는 모든 곳의 방문하여 거리를 구하고 배열에 넣는다. 이후 배열을 최솟값으로 정렬 한 후 배열을 리턴한다.
리턴한 배열을 가지고 좌표를 갱신하고 엄마 상어를 부르는 조건이 될때까지의 시간을 구하면된다.

"""

from collections import deque

N = int(input())

grid = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for i in range(N):
    data = list(map(int,input().split()))
    grid.append(data)
# 상어 좌표 넣기
q = deque()
shark_pos_r = 0
shark_pos_c = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            shark_pos_r = i
            shark_pos_c = j
            q.append((i,j,2))
            break
eat = 0
answer = 0
weight = 2
tmp_fish_pos = []
#먹을수 있는 생선 거리 구하기
def bfs(s_r, s_c, weight):
    q = deque([(s_r,s_c,weight,0)])
    tmp_fish_pos = []
    visited = [[False] * N for _ in range(N)]
    visited[s_r][s_c] = True
    while q:
        shark_pos_r, shark_pos_c, weight, dist = q.popleft()
        for i in range(4):
            n_s_r = shark_pos_r + dr[i]
            n_s_c = shark_pos_c + dc[i]
            if 0<=n_s_r<N and 0<=n_s_c <N:
                # 이동하면서
                if  not visited[n_s_r][n_s_c] and 0<=grid[n_s_r][n_s_c] <=weight:
                    visited[n_s_r][n_s_c] = True
                    q.append((n_s_r, n_s_c, weight, dist+1))
                    # 먹을 수 있는 생성 좌표 저장한다.
                    if 1<= grid[n_s_r][n_s_c] < weight:
                        tmp_fish_pos.append((dist+1,n_s_r,n_s_c))

    if len(tmp_fish_pos) >= 2:
        tmp_fish_pos.sort()
    return tmp_fish_pos 

while 1:
    # 먹을 수있는 생선 리스트 가지고온다. 거리순으로 정렬되어있다.
    edible_fish_list = bfs(shark_pos_r, shark_pos_c,weight)
    # 없으면 종료
    if len(edible_fish_list)==0:
        break
    # 만약 먹을게 있다면 먹는다
    eat+=1
    if eat == weight:
        weight +=1
        eat = 0
    #이전 상어 위치 초기화
    grid[shark_pos_r][shark_pos_c] = 0
    answer += edible_fish_list[0][0]
    shark_pos_r = edible_fish_list[0][1]
    shark_pos_c = edible_fish_list[0][2]
        
print(answer)