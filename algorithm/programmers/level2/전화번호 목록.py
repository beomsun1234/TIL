"""
Input  - 전화번호부에 적힌 전화번호를 담은 1차원 정수 배열 phone_book 
Output - 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true -> bool

DS - Hash

접두사가 같은지 판별하는 문제이다

1. 전화번호가 key이고 값이 1인 (key,value)딕셔너리를 만들어준다.
2. 반복문으로 비교할 전화번호를 찾고 해당 번호를 확인한다. 해당 번호가 해쉬맵에 key와 같은게 있다면 접두사가 같은 것이된다. 그러기에 return False 없으면 True

# 회고
처음에 해쉬와 완탐으로 접근했다. key를 해당 번호의 인덱스로주고 value를 전화번호로 맵을 만들었다. 효율설 검사 3,4를 통과하지 못했다.. 다른 방법으로 dfs를 사용해 보았지만 역시나 전 보다 더 많은 시간이 걸려서 시간초과가 나왔다.. key를 전화번호로 두었더니 모두 통과됐다. 

answer = True
    map = {}
    for idx,val in enumerate(phone_book):
        map[idx] = val
        
    for i in range(len(phone_book)):
        for j in range(i,len(phone_book)):
            if i!=j:
                if map.get(j).startswith(map.get(i)):
                    return False
                    
----
dfs
    map = {}
    ret = []
    global ck
    global flag
    flag = 0
    ck = True
    for idx,val in enumerate(phone_book):
        map[idx] = val
    visited = [False] * len(phone_book)
    def dfs(depth,map,val,visited):
        global ck,flag
        if flag ==1:
            return
        else:
            for i in range(len(phone_book)):
                if not visited[i]:
                    visited[i] = True
                    if map.get(i).startswith(val):
                        print(map.get(i),val)
                        ck = False
                        flag = 1
                    dfs(depth+1,map,map.get(i),visited)
                    visited[i] = False
    val = map.get(0)
    visited[0]=True
    dfs(0,map,val,visited)
"""
from collections import deque
def solution(phone_book):
    answer = True
    map = {}
    for idx,val in enumerate(phone_book):
        map[val] = idx
    
    
    for phone_number in phone_book: 
        jubdoo = "" 
        for number in phone_number: 
            jubdoo += number 
            if jubdoo in map and jubdoo != phone_number:                   return False
            
    return answer