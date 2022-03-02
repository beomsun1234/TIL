"""
14890 경사로 

문제를 이해를 못했었다.. 그래서 처음 작성한 코드를 보면 완전 이상한 조건이 포함되어 있었다.. 해당문제에 대해 설명한 내용을 읽고서야 이해할 수 있었다..
높은 곳에서는 아무것도 못하는 줄 알았지만 높은곳에서 바로보고 낮은 곳에 설치 할 수 도 있었다. 예를 들면

2
2
3
3
2
2

이 부분이였다. L이 2라고 한다면 처음 내가 생각했던 방식으로는 이부분은 지나갈수 없는 다리였다.. 높은곳에서 바로보고 조건이 맞다면 낮은 곳에 설치 할 수 있으므로
즉 4번 row에서 5,6번의 높이차가 1이고 낮은곳이 L만큼 연결 되어있으므로 갈 수 있다. 경사로를 놓았다면 놓았다는 표시를 해주어야하는데 처리를 해주지 않았다.. 문제를 자세히 읽어야겠다.. 

"""
N, L = map(int, input().split())

grid = []

for i in range(N):
    data = list(map(int,input().split()))
    grid.append(data)


# 가로 세로, 확인
def check_go(dirs):
    visited = [False] * N
    for i in range(1,N):
        # 만약 다음 가려는 곳이 같지 않다면
        if dirs[i-1] != dirs[i]:
            #높이가 차이가 1이 아니면 안된다.
            if abs(dirs[i-1] - dirs[i]) != 1:
                return False
            # 다음 위치가 높은 곳 일 경우
            if dirs[i-1] < dirs[i]:
                for j in range(1,L+1):
                    # 범위를 벗어나면 놓을 수 없다.
                    if i -j  <0:
                        return False
                    # 경사로를 놓는 곳이 L만큼 이어져있지 않다면 놓을 수 없다
                    if dirs[i-1] != dirs[i-j]:
                        return False
                    # 이미 경사로를 놓았을 경우
                    if visited[i-j]:
                        return False 
                    visited[i-j] = True
                
            elif dirs[i-1] > dirs[i]:
                for j in range(L):
                    # 범위를 벗어나면 놓을 수 없다.
                    if i +j >=N:
                        return False
                    # 경사로를 놓는 곳이 L만큼 이어져있지 않다면 놓을 수 없다
                    if dirs[i+j] != dirs[i]:
                        return False
                    # 이미 경사로를 놓았을 경우
                    if visited[i+j]:
                        return False
                    visited[i+j] = True
                        
    return True
ret = 0
# 가로
for i in range(N):
    if check_go(grid[i]):
        ret+=1
#세로
for i in range(N):
    col = []
    for j in range(N):
        col.append(grid[j][i])
    if (check_go(col)):
        ret+=1

print(ret)