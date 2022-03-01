"""
14499 주사위 굴리기

간단했다. 이 문제에서 가장 포인트는 주사위 굴리기 이다. 나의 주사위 굴리기 접근 방식은 이렇다.
주사위의 밑부분을 제외한 5가지 면을 2개의 배열로 저장해 주었다. 아래는 주사위의 전개도이다.
  2
4 1 3
  5
  6
내 접근은 2 1 5을 cube_r이라는 배열에 순서대로 저장하고, 4 1 3을 cube_c라는 배열에 순서대로 저장한다.
여기서 중요한 부분이 cube_r과 cube_c의 2번째 인덱스는 즉 cube_r[1], cube_c[1]은 값을 공유하며 맨 위쪽이 된다.
이제 밑 면을 나타내주는 bottom을 선언해준다. 

만약 북쪽으로 이동한다면 주사위의 모양은 아래와 같이 될 것이다.
  1
4 5 3
  6
  2
cube_r이 [2,1,5]에서 [1,5,6]으로 변할 것이다. 바텀은 6에서 2로 변경될 것이다. 자세히 보면 cube_r의 첫번째 인덱스가 바텀이되고
바텀은 cube_r의 마지막인덱스가 된다. 이걸 코드로 변환하면 아래와 같이 될 것이다.
tmp = bottom # 바텀에 있는 수 저장 
bottom = cube_r.popleft()
cube_r.append(tmp)

아래의 주사위를 남쪽으로 이동해 보자.
  2             6
4 1 3   ->    4 2 3  
  5             1
  6             5

이런식으로 변경 될 것이다. 변경된 모습을 자세히 보면 cube_r이 [2,1,5]에서 [6,2,1]으로 변할 것이고 바텀은6에서 5가 된다.
즉 밑 면이 첫번째 인덱스로 오고, 현재 cube_r의 마지막 인덱스가 바텀으로 변경 될 것이다.
이것을 코드로 변환하면 아래와 같이 될 것이다.
tmp = bottom
bottom = cube_r.pop()
cube_r.appendleft(tmp)

아래의 주사위를 동으로 이동해 보자.
  2             2
4 1 3   ->    6 4 1   
  5             1
  6             3

위와 같이 변경 될 것이다. 변경된 모습을 자세히 보면 cube_c가 [4,1,3]에서 [6,4,1]으로 변할 것이고 바텀은6에서 3이 된다.
즉 밑 면이 첫번째 인덱스로 오고, 현재 cube_c의 마지막 인덱스가 바텀으로 변경 될 것이다.
이것을 코드로 변환하면 아래와 같이 될 것이다.
tmp = botom
botom = cube_c.pop()
cube_c.appendleft(tmp)


서쪽은 북쪽과 같은 식으로 변경하면 된다. 위 방법으로 주사위를 굴리며 이동하고 큐브의 맨위의 값(cube_r[1] 또는 cube_c[1])을 출력하면된다.


"""

from collections import deque
N, M, start_r, start_c, K = map(int,input().split())
# 주사위
# cube_r[1] = 윗면
botom = [0]
cube_r = deque([0,0,0])
# cube_c[1] = 윗면 두개 공유
cube_c = deque([0,0,0])
grid = []
for i in range(N):
    data = list(map(int,input().split()))
    grid.append(data)
d = list(map(int,input().split()))


#0 동,1서,2북, 3남
dirs = ((0,1),(0,-1),(-1,0), (1,0))

def move(dir):
    # 동쪽으로 구르기
    if dir == 1:
        tmp = botom[0]
        botom[0] = cube_c.pop()
        cube_c.appendleft(tmp)
        cube_r[1] = cube_c[1]
        top = cube_c[1]
    #서쪽으로 구르기
    elif dir == 2:
        tmp = botom[0]
        botom[0] = cube_c.popleft()
        cube_c.append(tmp)
        cube_r[1] = cube_c[1]
        top = cube_c[1]
    # 북쪽으로 구르기
    elif dir == 3:
        tmp = botom[0]
        botom[0] = cube_r.popleft()
        cube_r.append(tmp)
        cube_c[1] = cube_r[1]
        top = cube_r[1]
    # 남쪽으로 구르기
    elif dir == 4:
        tmp = botom[0]
        botom[0] = cube_r.pop()
        cube_r.appendleft(tmp)
        cube_c[1] = cube_r[1]
        top = cube_r[1]

    return top

for i in d:
    next_r = start_r +dirs[i-1][0]
    next_c = start_c +dirs[i-1][1]
    if 0<= next_r < N and 0<= next_c<M:
        if grid[next_r][next_c] == 0:
            print(move(i))
            grid[next_r][next_c] = botom[0]
        elif grid[next_r][next_c] >0:
            print(move(i))
            botom[0] = grid[next_r][next_c]
            grid[next_r][next_c] = 0
        start_r = next_r
        start_c = next_c