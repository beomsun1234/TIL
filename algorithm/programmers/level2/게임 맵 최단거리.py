"""
level 2 - 게임 맵 최단거리(찾아라 프로그래밍 마에스터)
bfs- 최단거리
정말 간단했다. bfs를 이용해서 최단거리를 마킹해나가면서 상대방 진영인 (n,m) 위치에 도달했을 경우 해당 값을 리턴하면 된다. 만약 도달하지 못하면 -1을 리턴해주었다.

도달하지 못할 경우 마킹을 하지 못하므로 마킹 전에 초기값인 무한대 일 경우가 도달하지 못한 경우이다.
"""
from collections import deque
def solution(maps):
    answer = 0
    visited = [[float('inf')]*len(maps[0]) for _ in range(len(maps))]
    # 이동 방향
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    # 항상 0,0에서 시작한다
    q = deque()
    q.append((0,0,1)) # 시작 위치 값은 1
    visited[0][0] = 1 # 시작 위치 값은 1
    while q:
        x,y,c = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < len(maps) and ny >= 0 and ny < len(maps[0]):
                if maps[nx][ny] == 0: # 벽이면 넘어간다
                    continue
                if visited[nx][ny] > c+1: #현재 방문한 곳에 거리 값 +1 )이 다음 방문할 거리 보다 작으면 다음 방문 거리의 값을 갱신한다. 
                    visited[nx][ny] = c+1 
                    q.append((nx,ny,c+1))
    
    if visited[-1][-1] == float('inf'):
        return -1
    return visited[-1][-1]
    
