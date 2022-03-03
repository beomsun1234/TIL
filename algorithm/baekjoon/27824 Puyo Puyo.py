"""
27824 Puyo Puyo

간단했지만 문제가 살짝 까다로웠다. 로직은 이렇다. bfs로 상하좌우로 4개이상 연결되어있는 같은 색 뿌요들을 찾는다.
찾은다음 뿌요를 삭제하고 삭제가 완료되면 아래로 떨어지게 만든다. 더 자세한 로직은
우선 bfs로 탐색하여 4개이상 연결된 지점들의 좌표를 저장하고 return한다. 만약 연결된게 4개이상이 아니라면 0을 리턴한다.
이 후 좌표를 set를 변환해준다. 중복되는 좌표가 존재하기 때문이다. 아를 위해 set을 사용하며 이 좌표를 row의 내림차순으로 정렬한다. 
중력에 의해 떨어지는 것을 구현하기위해 row를 내림 차순으로 정렬해주었다. 아래와 같이 뿌요들이 있다고 하면 처음 탐색시 R로 이루어진 뿌요를 삭제할 수 있다.

      .Y....       .Y....
      .YG...       .YG...
      RRYG..   ->  ..YH..
      RRYGG.       ..YGG.

이후 Y를 내리기 위해서는 R들의 좌표 중에 row가 가장 작은 값부터 내려야 하기에 내림 차순으로 정렬하고 뿌요를 아래로 떨어지게했다.

4개이상 같은 색으로 연속되어있는 뿌요들을 삭제하고 내린 후 answer +1 해주면 정답을 도출할 수 있다.

"""

from collections import deque
import copy
dr = [1,-1,0,0]
dc = [0,0,1,-1]
global ret
ret = 0
grid = []
for i in range(12):
    data = list(input())
    grid.append(data)

def bfs(s_r,s_c,color):
    global ret
    q = deque()
    q.append((s_r,s_c))
    cnt = 0
    tmp_pos = []
    visited = [[False]*6 for _ in range(12)]
    while q:
        now_r, now_c = q.popleft()
        for i in range(4):
            next_r = now_r + dr[i]
            next_c = now_c + dc[i]
            if 0<=next_r<12 and 0<= next_c <6:
                if not visited[next_r][next_c] and grid[next_r][next_c] == color:
                    cnt+=1
                    q.append((next_r,next_c))
                    tmp_pos.append((next_r,next_c))
                    visited[next_r][next_c] = True
    # 4개이상 뭉쳐있다면 해당 좌표들 저장
    global check
    if cnt >= 4:
        ret+=1
        check= True
        return tmp_pos
    return 0
answer = 0
tt_pos = []
global check
check = False
flag = True
while flag:
    for i in range(12):
        for j in range(6):
            if grid[i][j] != '.':
                data = bfs(i,j,grid[i][j])
                # 4개 이상 뭉쳐있따면
                if data !=0:
                    tt_pos.extend(data)
        
    # 터진다.
    ttt_pos = set(tt_pos)
    ttt_pos = sorted(ttt_pos)
    tmp_grid = copy.deepcopy(grid)
    # 뿌요 삭제
    for rr, cc in ttt_pos:
        grid[rr][cc] = '.'
    # 터진 후 아래로 떨어진다
    for rr,cc in ttt_pos:
        for k in range(rr,0,-1):
            grid[k][cc] = tmp_grid[k-1][cc]
            tmp_grid[k][cc] = grid[k][cc]
        grid[0][cc] = '.'
    tt_pos = []
    # 없어질 뿌요가 없다면 종료
    if not check:
        flag = False
        break
    ret = 0
    check = False
    answer+=1
print(answer)