"""
20055 컨베이어 벨트 위의 로봇
"""

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split())

conveyor_belt = deque(list(map(int, input().split())))
robot = deque([False]*N)

step = 1
#첫번재 
while 1:
    """
    1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    """
    # 벨트회전
    conveyor_belt.appendleft(conveyor_belt.pop())
    # 로봇회전
    robot.appendleft(robot.pop())
    # 로봇이 내리는위치에 도달하면 내린다.
    if robot[N-1] == True:
        robot[N-1] = False
    """
    2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    """
    # 내려가는 부분이 i-1이므로 그전부터 진행
    for i in range(N-2, -1,-1):
        if robot[i] == True and conveyor_belt[i+1] >=1 and not robot[i+1]:
            conveyor_belt[i+1] -=1
            robot[i+1] = True
            robot[i] = False
    # 내리는위치에 도달하면 내린다.
    robot[-1] = False

    """
    3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    """
    if conveyor_belt[0] >0 and not robot[0]:
        robot[0] = True 
        conveyor_belt[0]-=1

    """
    4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    """  
    # 0인 내구도의 개수가 k개 이상이면 종료
    if conveyor_belt.count(0) >= K:
        break
    step +=1

print(step)