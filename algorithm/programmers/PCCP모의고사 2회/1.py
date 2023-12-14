# 1번
def solution(command):
    answer = []
    dir = 1

    dx = [-1,0,1,0,-1]
    dy = [0,1,0,-1,0]
    x = 0
    y = 0
    for c in command:    
        if c == "G":
            x = x + dx[dir%4]
            y = y + dy[dir%4]
        elif c == "B":
            x = x - dx[dir%4]
            y = y - dy[dir%4]
        elif c == "R":
            dir +=1
        elif c == "L":
            dir +=3
    answer.append(x)
    answer.append(y)
    return answer
