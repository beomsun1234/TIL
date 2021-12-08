"""
완탐 level2, 소수찾기 
"""
def isPrime(n):
    if n ==0:
        return False
    if n == 1:
        return False
    for i in range(1,n):
        if i != 1:
            if n % i == 0:
                return False
    return True

def dfs(idx,num,ret,numbers,visited,pick):
    # 처음시작할때 ''로 초기화 하기에 num이 ''아니거나 0으로 시작하지 않거나,소수일때 해당 값
    # set자료구조에 저장한다
    if num != '' and not num.startswith('0') and isPrime(int(num)):
        ret.add(num)
    for i in range(0,len(numbers)):
        if not visited[i]:
            visited[i] = True
            num+=numbers[i]
            dfs(i,num,ret,numbers,visited,pick+1)
            num = num[:-1]
            visited[i] = False
    
def solution(numbers):
    answer = 0
    ret = set([])
    visited = [False] * len(numbers)
    dfs(0,"",ret,numbers,visited,0)
    print(ret)
    return len(ret)
    
--------