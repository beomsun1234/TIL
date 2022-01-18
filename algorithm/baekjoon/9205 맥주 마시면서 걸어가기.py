"""
맥주 마시면서 걸어가기
간단했지만..처음에 제출했지만 통과되지 못했었다.. 코드를 자세히 보니 방문했던 편의점에 대해서 방문처리를 해주지 않아서 통과하지못했다.. set을 만들어서 편의점 방문 표시를 해주었다.

내 로직은 이렇다

상근이 집에서 시작해서 들를수( 두 좌표 사이의 거리는 x 좌표의 차이 + y 좌표의 차이 이다. <= 50*20(맥주개수)) 있는 편의점의 좌표를 갱신해서 최종적으로 방문한 편의점의 좌표에서 출발할 경우 맥주를 마시면서 목적지까지 갈 수 있는지 확인 하여 가능하면 flag에 1을 주어
happy, flag = 0 -> sad가 된다.



"""
from collections import deque

t = int(input())

for _ in range(t):
    # 편의점 개수
    n = int(input())
    # 상근이 집
    start_x , start_y = map(int, input().split())
    p = []
    # 편의점 좌표
    for i in range(n):
        p.append(list(map(int,input().split())))
    #목적지
    goal_x, goal_y = map(int,input().split())

    # 거리 구하기는 (x2-x1) + (y2-y1)
    def getDist(x2,y2,x1,y1):
        return abs(x2-x1) + abs(y2-y1)


    ## bfs를 통해서 가보자
    q = deque()
    q.append((start_x,start_y))

    bear_cnt = 20
    flag = 0
    visited = set()
    while q:
        now_x, now_y = q.popleft()
        if getDist(goal_x, goal_y, now_x, now_y) <= bear_cnt*50:
            flag = 1
            break
        for x,y in p:
            if (x,y) not in visited:
                dist = getDist(x,y, now_x, now_y)
                if  dist <= bear_cnt *50: # 50미터당 맥주 1개이므로
                    next_x = x
                    next_y = y
                    q.append((next_x,next_y))
                    visited.add((x,y))

    if flag == 1:
        print('happy')
    else:
        print('sad')
