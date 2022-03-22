"""
프로그래머스 2021 카카오 채용연계형 인턴십 - 표 편집

실패
"""
from collections import deque

def getFrontIdx(idx,state):
    tmp_idx = idx
    while tmp_idx>0:
        tmp_idx -=1
        if not state[tmp_idx]:
            return tmp_idx

def getBackIdx(idx,state):
    #위
    tmp_idx = idx
    while tmp_idx < len(state):
        tmp_idx +=1
        if not state[tmp_idx]:
            return tmp_idx
    
def solution(n, k, cmd):
    answer = ''
    state = [False] * n
    cursor = k
    l_idx = n-1 
    #(행번호,이름)
    delete_history = deque()
    for c in cmd:
        tt = c.split(" ")
        op = tt[0]
        if op == 'U' or op == 'D':
            cnt = int(tt[1])
            tmp = cnt
            tmp_cur = cursor
            if op == 'U':
                for i in range(cnt):
                    tmp_cur-=1
                    if state[tmp_cur]:
                        tmp+=1
                cursor = cursor - tmp
            elif op == 'D':
                for i in range(cnt):
                    tmp_cur+=1
                    if state[tmp_cur]:
                        tmp+=1
                cursor = cursor + tmp
        elif op == 'C':
            state[cursor] = True
            delete_history.append(cursor)
            if cursor == l_idx:
                cursor = getFrontIdx(cursor,state)
                l_idx = cursor
            else:
                cursor = getBackIdx(cursor,state)
        else:
            undo_idx = delete_history.pop()
            state[undo_idx] = False
            if undo_idx > l_idx:
                l_idx = undo_idx
    answer = ['O'] * n
    while delete_history:
        del_idx = delete_history.popleft()
        answer[del_idx] = 'X'
    return "".join(answer)