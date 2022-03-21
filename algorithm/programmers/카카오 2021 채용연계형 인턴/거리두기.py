"""
프로그래머스 2021 카카오 채용연계형 인턴십 - 거리두기
"""

from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def bfs(start_r,start_c,grid):
    q = deque()
    visited = [[False] * 5 for _ in range(5)]
    q.append((start_r, start_c,0))
    visited[start_r][start_c] = True
    distance = [[10000] * 5 for _ in range(5)]
    tmp_p = []
    while q:
        now_r, now_c, dist = q.popleft()
        # 2이상인 거리는 볼 필요가 없다.
        if dist>=2:
            break
        for i in range(4):
            next_r = now_r + dr[i]
            next_c = now_c + dc[i]
            next_dist = dist +1
            if 0<=next_r<5 and 0<=next_c<5 and not visited[next_r][next_c]:
                visited[next_r][next_c] = True
                if grid[next_r][next_c] == 'O':
                    q.append((next_r,next_c, next_dist))
                # 만약 다음 방문 할 곳에 사람이 앉아있으면
                elif grid[next_r][next_c] == 'P':
                    #거리가 2보다 작거나 같다면
                    if dist<=2:
                        return False
    
    return True
        

def solution(places):
    answer = []
    for i in places:
        grid = []
        for k in i:
            grid.append(list(k))
        flag = False
        for rr in range(5):
            for cc in range(5):
                # 응시자가 앉아있는 자리를 기준으로 맨하탄 거리가 2이하인 응시자를 찾는다.
                if grid[rr][cc] == 'P':
                    if not bfs(rr,cc,grid):
                        flag = True
                        break
        if not flag:
            answer.append(1)
        elif flag:
            answer.append(0)
        
    return answer