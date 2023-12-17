# 3번
def solution(menu, order, k):
    answer = 0
    time = 0
    inCome = 0
    cook_time = 0
    cook = []
    start = 0
    while start < len(order):
        if inCome <= time:
            menu_idx = order[start]
            cook_time = menu[menu_idx]
            inCome += k
            time += cook_time
            cook.append(time)
            start +=1
        else:
            time +=1
    step = 0
    per = len(order)
    maxRes = 0
    start = 1
    r = 1
    while cook:
        w = 0
        c = cook.pop(0)
        start = r
        while start < per:
            inCC = start*k

            if c - inCC <=0:
                break
            w+=1
            start +=1
        r +=1
        maxRes = max(maxRes, w)
    answer = maxRes +1
    return answer
