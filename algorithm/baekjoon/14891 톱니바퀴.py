"""
14891 - 톱니바퀴

"""

from collections import deque

gear = []

for _ in range(4):
    data = list(map(int,input()))
    gear.append(data)
# 확인 할게 
# 1번 톱니의 2번 인덱스(3)와 2번 톱니의 6번 인덱스(7)
# 2번톱니의 2번인덱스(3)와 3번톱니의 6번인덱스(7)
# 3번톱니의 2번인덱스(3)와 4번톱니의 6번인덱스(7)
# 둘이 같지 않으면 회전x 같다면 현재 톱니의 회전에 반대회전
k = int(input())
spin = []
for _ in range(k):
    data = list(map(int, input().split()))
    # 0은 회전 기준 톱니, 1은 회전방향 -> -1 시계반대, 1 시계
    spin.append((data[0],data[1]))

def get_spin_number(base_num,dir):
    tmp = []
    dd = []
    tt = dir
    if base_num == 1:
        if gear[0][2] != gear[1][6]:
            dd.append(-1*dir)
            dir = -1*dir
            tmp.append(2)
            if gear[1][2] != gear[2][6]:
                dd.append(-1*dir)
                dir = -1*dir
                tmp.append(3)
                if gear[2][2] != gear[3][6]:
                    dd.append(-1*dir)
                    tmp.append(4)
    elif base_num == 2:
        if gear[0][2] != gear[1][6]:
            dd.append(-1*dir)
            tmp.append(1)
        if gear[1][2] != gear[2][6]:
            dd.append(-1*dir)
            dir = -1*dir
            tmp.append(3)
            if gear[2][2] != gear[3][6]:
                dd.append(-1*dir)
                tmp.append(4)
    
    elif base_num == 3:
        if gear[1][2] != gear[2][6]:
            dd.append(-1*dir)
            dir = -1*dir         
            tmp.append(2)
            if gear[0][2] != gear[1][6]:
                dd.append(-1*dir)
                tmp.append(1)
        if gear[2][2] != gear[3][6]:
            dd.append(-1*tt)
            tmp.append(4)

    elif base_num == 4:
        if gear[2][2] != gear[3][6]:
            dd.append(-1*dir)
            dir = -1*dir   
            tmp.append(3)
            if gear[1][2] != gear[2][6]:
                dd.append(-1*dir)
                dir = -1*dir   
                tmp.append(2)
                if gear[0][2] != gear[1][6]:
                    dd.append(-1*dir)
                    tmp.append(1)
        
    return tmp,dd

def spin_gear(start_num, dir):
    spin_number,spin_dir = get_spin_number(start_num,dir)
    # 시작 톱니 회전
    tmp = gear[start_num-1]
    q = deque(tmp)
    if dir == 1: #시계방향
        tt = q.pop()
        q.appendleft(tt)
    else: # 반시계 앞에꺼 때서 뒤로
        tt = q.popleft()
        q.append(tt)
    gear[start_num-1] = list(q)
    # 회전시킬 톱니 회전
    for i in range(len(spin_number)):
        tmp = gear[spin_number[i]-1]
        q = deque(tmp)
        if spin_dir[i] == 1: #시계방향
            tt = q.pop()
            q.appendleft(tt)
        else: # 반시계 앞에꺼 때서 뒤로
            tt = q.popleft()
            q.append(tt)
        gear[spin_number[i]-1] = list(q)
    

for t_number, sp in spin:
    spin_gear(t_number,sp)

answer =  gear[0][0] + gear[1][0] * 2 + gear[2][0] * 4 + gear[3][0] * 8

print(answer)
