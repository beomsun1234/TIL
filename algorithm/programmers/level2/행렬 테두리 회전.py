"""
프로그래머ㅡlevel2 - 행렬 테투리 회전.py

처음에 문제를 보고 많이 접해보지 못해서 당황했지만 조금만 생각하면 쉬웠다. 주어진 내용 대로 구현하면 됐다. 나는 우선 grid라는 rows x columns 행렬을 만들주고 1씩증가하면서 값을 넣어 주었다. 이후 모두 0으로 초기화된 grid_copy라는 배열을 만들어 주고 변한 값을 grid_copy에 복사하고 시계방향 회전이 종료되면 grid배열에 매치 시켜주었다. 복사하는 로직은 위에서 부터 시작하며 시계방향이므로 위쪽일 경우에 로우 고정에 -> 방향이므로 현재 컬럼에 이전 컬럼을 복사해 주었다. 이후 오른쪽 방향으로 향하고 오른쪽은 아래로 향하므로 컬럼값 고정에 현재 로우에 이전 로우 값을 복사해준다. 이후 바텀 방향으로 향하며 바텀은 로우 고정에 <- 방향이므로 이전 컬럼에 현재 컬럼을 복사한다. 마지막으로 왼쪽 방향으로 향하며 왼쪽은 컬럼 고정에 위로 향하므로 이전 로우에 현재 로우 값을 복사해준다. 

"""
def changeGrid(grid_copy, grid):
    init_grid_copy = []
    for i in range(len(grid)):
        init_grid_copy.append([])
        for j in range(len(grid[0])):
            init_grid_copy[i].append(0)
            if grid_copy[i][j] !=0:
                grid[i][j] = grid_copy[i][j]            
    return grid,init_grid_copy
    

def solution(rows, columns, queries):
    answer = []
    cnt=1
    minVal = 10001
    grid = []
    grid_copy = []
    for i in range(rows):
        grid.append([])
        grid_copy.append([])
        for j in range(columns):
            grid[i].append(cnt)
            cnt+=1
            grid_copy[i].append(0)
        
    # 4가지 방향을 배열 값을 바꿔주자
    # up
    # dowun
    # left
    # right
    for r1,c1,r2,c2 in queries:
        ## top(로우가 같다)
        for i in range(c1,c2):
            tmp = grid[r1-1][i-1]
            grid_copy[r1-1][i] = tmp
        ## right(컬럼이 같다)
            minVal = min(minVal,tmp)
        for i in range(r1,r2):
            tmp = grid[i-1][c2-1]
            grid_copy[i][c2-1] = tmp
            minVal = min(minVal,tmp)
        ## bottom(로우가 같다)
        for i in range(c2-1,c1-1,-1):
            tmp = grid[r2-1][i]
            grid_copy[r2-1][i-1] = tmp
            minVal = min(minVal,tmp)
        ## left(컬럼이 같다)
        for i in range(r2-1,r1-1,-1):
            tmp =grid[i][c1-1]
            grid_copy[i-1][c1-1] = tmp
            minVal = min(minVal,tmp)
        grid,grid_copy = changeGrid(grid_copy, grid)
        answer.append(minVal)
        minVal = 10001
    
    return answer