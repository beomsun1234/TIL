from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    for idx, p in enumerate(priorities):
        q.append((p,idx))
    
    while q:
        item = q.popleft()
        if item[0] < max(q)[0]:
            q.append(item)
        else:
            answer+=1
            if item[1] == location:
                break
            
    return answer
            