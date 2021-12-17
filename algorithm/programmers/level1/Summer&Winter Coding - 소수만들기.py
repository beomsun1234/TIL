"""
level 1 Summer/Winter Coding(~2018)

소수만들기

"""
def isPrime(num):
    flag = 0
    if num == 0:
        return False
    if num == 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            flag = 1
            break
    if flag ==1:
        return False
    return True

def dfs(pick,idx,ret,nums,visited):
    global answer
    if pick == 3:
        if isPrime(sum(ret)):
            answer+=1
        return
    for i in range(idx,len(nums)):
        if not visited[i]:
            ret.append(nums[i])
            visited[i] = True
            dfs(pick+1,i, ret,nums,visited)
            ret.pop()
            visited[i] = False

def solution(nums):
    global answer
    answer = 0
    visited = [False] * len(nums)
    ret = []
    dfs(0,0,ret,nums,visited)
    return answer
    