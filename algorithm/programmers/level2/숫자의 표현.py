"""

프로그래머스 level 2- 숫자의 표현
처음 제출한 코드는 15를 만들수 있는 모든 경우의 수를 찾고 해당 경우의 수 중 연속되는 숫자인지 판별하는 코드 이다.. 이렇게 작성하면 3문제만 통과되고 전부 시간 초과가 발생한다.. 당연하다 n이 10000이하이기에 n이 10000일 경우 내코드는 시간복잡도가 O(2*10000) 정도될 것이다.. 재귀 및 dfs 연습하려고 무작정 dfs만 사용하는 것 같다.. 항상 경우의 수를 구하려고하면 dfs만 작성한다.. 좀더 신중하게 방법을 고안해야겠다... 완전 탐색으로 충분히 가능 할 것 같았다. 로직은 이렇다 1~n의 숫자부터 시작해서(i), 연속된 숫자(i,n+1) 를 sum에 더해준다. sum이 n이되면 연속된 숫자가 된다.

def isContinue(nums):
    check = 0
    tmp = 0
    for i in range(0, len(nums)):
        if nums[i] - tmp == 1 or nums[i] - tmp == nums[i]:
            check+=1
            tmp = nums[i]
        else:
            break
 
    if check == len(nums):     
        return True
    
    return False
    
    

def dfs(idx,ret,n):
    global answer
    if sum(ret) > n:
        return
    if sum(ret) == n:
        if len(ret) == 0:
            answer+=1
            return
        if isContinue(ret):
            answer+=1
            return
        return
    for i in range(idx,n+1):
        ret.append(i)
        dfs(i+1,ret,n)
        ret.pop()

def solution(n):
    global answer
    answer = 0

    ret = []
    dfs(1,ret,n)
    
    return answer

"""

def solution(n):
    answer = 0
    for i in range(1,n+1):
        sum = 0
        for j in range(i,n+1):
            sum+=j
            if sum == n:
                answer +=1
                break
            if sum > n:
                break
    return answer