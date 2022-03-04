"""
15685 드래곤 커브
"""
#드래곤 커브 개수
N = int(input())
"""
방향
0: x좌표가 증가하는 방향 (→)
1: y좌표가 감소하는 방향 (↑)
2: x좌표가 감소하는 방향 (←)
3: y좌표가 증가하는 방향 (↓)
"""
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# d가 0,2 현재 끝좌표에 선을 세운다
# d가 1,3 현재 끝좌표에 선을 눞힌다
visited = [[False]*(101) for _ in range(101)]
def make_dragon_curve(x,y, start_d):
    visited[x][y] = True
    dirs = [start_d]
    #드래곤 커브 방향 저장
    for i in range(g):
        tmp = []
        for j in range(len(dirs)):
            tmp.append((dirs[-j - 1] + 1) % 4)
        dirs.extend(tmp)
    
    """
0: x좌표가 증가하는 방향 (→)
1: y좌표가 감소하는 방향 (↑)
2: x좌표가 감소하는 방향 (←)
3: y좌표가 증가하는 방향 (↓)
    """
    for i in dirs:
        nx = x+ dx[i]
        ny = y + dy[i]
        visited[nx][ny] = True
        x = nx
        y = ny

for i in range(N):
    x,y,d,g = map(int,input().split())
    make_dragon_curve(x,y,d)

answer = 0
for i in range(100):
    for j in range(100):
        # 꼭지점에 드래곤커브가 있다면
        if visited[i][j] and visited[i + 1][j] and visited[i][j + 1] and visited[i + 1][j + 1]:
            answer += 1

print(answer)