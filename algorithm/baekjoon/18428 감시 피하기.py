"""
18428 - 감시 피하기

처음 접근은 학생 시점으로 생각했다. 즉 현재 학생의 위치를 기준으로 상하 좌우 모든 칸을 보고 선생님이 있으면 학생 앞에 장애물을 놓는 방식으로 접근했다.
제출하니 20퍼에서 실패가 발생했다..  맞왜틀이 발생한거다... 분명 맞았는데 왜 틀렸지?? 다른 접근으로 장애물을 빈 공간에 무작위로 3개 놓는다. 그리고 나서 
선생님을 기준으로 학생을 찾는다. 학생을 찾으면 false를 리턴하고 4방향 모두 발견하지 못하면 true를 리턴한다. 모든 선생님이 true를 리턴할 경우 dfs를 종료하고 정답을 리턴한다.
"""
N = int(input())

grid = []
dr = [1,-1,0,0]
dc = [0,0,1,-1]

for i in range(N):
    data = list(map(str,input().split()))
    grid.append(data)
walls_pos_combi = []

global cnt
cnt = 0

## 학생 찾기
def check(r,c):
    for i in range(4):
        # 0 = 위, 1 아래 , 2 왼 ,3 오
        if i == 0 and r >= 0:
            for i in range(r-1,-1,-1):
                if grid[i][c] == 'O':
                    break
                elif grid[i][c] == 'S':
                    return False
        elif i == 1 and r < N:
            for i in range(N-r):
                if grid[i+r][c] == 'O':
                    break
                elif grid[i+r][c] == 'S':
                    return False
        elif i == 2 and c >= 0:
            for i in range(c-1,-1,-1):
                if grid[r][i] == 'O':
                    break
                elif grid[r][i] == 'S':
                    return False
        elif i ==3 and c <N:
            for i in range(N-c):
                if grid[r][i+c] == 'O':
                    break
                elif grid[r][i+c] == 'S':
                    return False

    return True


global flag
flag = 0
def dfs(pick):
    global flag
    global cnt
    if flag == 1:
        return
    if pick == 3: # 무작위로 3개 놓았다면
        # 선생님을 기준으로 학생을 찾는다.
        for i in range(N): 
            for j in range(N):
                if grid[i][j] == 'T':
                    if not check(i,j):
                        cnt = 1
        if cnt == 0:
            flag = 1
        cnt = 0
        return
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'X':
                grid[i][j] = 'O'
                walls_pos_combi.append((i,j))
                dfs(pick+1)
                grid[i][j] ='X' # 백트래킹
                walls_pos_combi.pop()

dfs(0)
if flag == 1:
    print("YES")
else:
    print("NO")