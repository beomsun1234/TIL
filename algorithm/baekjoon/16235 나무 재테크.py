# 1x1 칸에 나무가 여러개 존재 가능. 
N, M, K = map(int,input().split())

# 땅에 5만큼 양분이 있다.
grid = [[5 for j in range(N)] for i in range(N)]

# x- 세로, y- 가로
global treeDB
treeDB = {}

# 양분
A = []

for i in range(N):
    A.append(list(map(int, input().split())))

for i in range(M):
    x, y, age = map(int,input().split())
    x= x-1
    y = y-1
    key = (x,y)
    if (x,y) in treeDB:
        treeDB[(x,y)].append(age)
    else:
        treeDB[(x,y)] = [age]

#print(treeDB)
#treeDB[(1,2)].append(4)


def 봄여름():
    """
    봄에는  나이만큼 양분을 먹고 나이가 1 증가한다.
     나이가 적은순서로 양분을 먹는다. 양분을 먹지 못한 나무는 죽는다....
    """
    global treeDB
    for x in range(N):
        for y in range(N):
            key = (x,y)
            if key not in treeDB:
                continue
            tmp = []
            #양분
            a = grid[x][y]
            g = 0
            val = treeDB[key]
            val.sort()
            for age in val:
                new_age = 0
                if a>=age:
                    # 양분을 먹고 
                    a -= age 
                    # 1살 증가
                    new_age = age+1 
                    tmp.append(new_age)
                else:                 
                    # 나이만큼 양분을 먹지못하면 죽는다... 죽은 나무는 여름에 양분으로 변한다.
                    treeToA = 여름(age)
                    g += treeToA
            grid[x][y] = a + g
            del treeDB[key]
            treeDB[key]= tmp

    

def 여름(age):
    """
    여름에는 봄에 죽은 나무가 양분으로 변하게 된다.
    각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 
    소수점 아래는 버린다.
    """
    #print("여름")
    tmp = age//2
    return tmp

dy = [1, 1,-1, -1, 1, -1, 0, 0]
dx = [1,-1, 1, -1, 0,  0, 1, -1]

def 가을():
    """
    가을에는 나무가 번식한다. 
    번식하는 나무는 나이가 5의 배수이어야 하며, 
    인접한 8개의 칸에 나이가 1인 나무가 생긴다. 
    어떤 칸 (r, c)와 인접한 칸은 이다. 
    (r-1, c-1), (r-1, c), 
    (r-1, c+1), (r, c-1),
    (r, c+1), (r+1, c-1), 
    (r+1, c), (r+1, c+1)
    상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
    """
    #print("가을")
    global treeDB
    for x in range(N):
        for y in range(N):
            key = (x,y)
            if key not in treeDB:
                continue
            val = treeDB[key]
            for age in val:
                # 5의 배수이면 번식한다.
                if age % 5 == 0:
                    #print("번식")
                    # 인접한 8개의 칸에 나이가 1인 나무가 생긴다
                    for i in range(8):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        if 0<= ny < N and 0<= nx <N:
                            #나무 생김
                            key = (nx,ny)
                            if key in treeDB:
                                treeDB[key].append(1)
                            else:
                                treeDB[key] = [1]
                        else:
                            continue 
                else:
                    continue



def 겨울():
    """
    겨울에는 초기에 입력받은 양분의 값이 추가된다.
    """
    #print("겨울")
    for i in range(N):
        for j in range(N):
            grid[i][j] += A[i][j]

for i in range(K):
    # first for loop is year
    봄여름()
    가을()
    겨울()

treeCnt = 0

for i in range(N):
    for j in range(N):
        key = (i,j)
        if key not in treeDB:
            continue
        else:
            val = treeDB[key]
            treeCnt += len(val)

print(treeCnt)
