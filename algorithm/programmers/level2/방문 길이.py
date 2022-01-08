"""
level2 - 방문길이
bfs를 이용했다.. 사실 bfs이용하지 않고 for하나만으로도 가능하다.. 정말 간단하게 생각했다. 처음에 좌표지점을 이용했고 해당 지점에 방문했는지 확인하는 로직이였다. 이렇게 하니 1~8까지만 통과하고 전부 실패하였다.. 질문하기에서 힌트를 보니 좌표로 생각하지 말고 경로를 생각해서 해당 경로를 사용했는지를 판별하도록 하라고 힌트를 주셨다. 즉 가는 방향과 오는 방향의 좌표값을 쌍으로 저장해야했다. set을 사용해서 가는 방향 오는 방향의 좌표를 저장하고 최종적인 set의 길이//2를 해주면 방문 길이를 알 수 있게 된다. 나누기 2 해주는 이유는 좌표값을 쌍으로 저장했기 때문이다

"""
from collections import deque
def solution(dirs):
    answer = 0
    # U 위, D 아래, R 오, L 왼
    # r-1   r +1   c +1  c-1
    # 0,0 에서 시작한다
    visited = set()
    q = deque()
    q.append((0,0))
    cnt = 0
    while q:
        r,c = q.popleft()
        if not dirs: # 방향을 전부 사용하면 종료
            break
        dir = dirs[0]
        nr = r
        nc = c
        tmpr = r
        tmpc = c
        if dir == 'U':
            nr +=1
        elif dir == 'D':
            nr -=1
        elif dir == 'L':
            nc -= 1
        elif dir == 'R':
            nc += 1
        # 범위를 벗어나면 해당 방향 제거하고 이전 r,c로 돌아간다.
        if nr < -5 or nr > 5 or nc <-5 or nc >5:
            dirs = dirs[1:]
            q.append((tmpr,tmpc))
            continue
        ## 양방향 좌표 가거나 오거나
        visited.add(((r, c),(nr,nc))) 
        visited.add(((nr,nc),(r, c)))
        
        dirs = dirs[1:]
        q.append((nr,nc))
    return len(visited)//2