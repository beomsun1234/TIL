"""
찾아라 프로그래밍 마에스터 폰켓몬 level 1

처음에 재귀로 완탐을 돌려서 모든 조합을 뽑아서 set에 집어넣고 길이를 체크했다.. 제약조건을 생각안하고 레벨을 보고 이거 그냥 풀어되 되겠다고 생각했다..
역시나 주어진 테케는 통과하나 제출하면 시간초과가 발생했다.. 풀면서 시간초과가 발생할 것이라 생각했지만 문제를 너무 낮게 봤다.. 아래는 틀린 코드이다..
def checkKinds(ret):
    check = set()
    for i in ret:
        check.add(i)
    return len(check)
        
def dfs(pick,idx,ret,nums,visited):
    if pick == len(nums)//2:
        global answer
        answer = max(answer,checkKinds(ret))
        print(checkKinds(ret))
    for i in range(idx,len(nums)):
        if not visited[i]:
            ret.append(nums[i])
            visited[i] = True
            dfs(pick+1,i,ret,nums,visited)
            visited[i] = False
            ret.pop()
def solution(nums):
    global answer
    answer = 0
    visited = [False] * len(nums)
    pickSize = len(nums)//2
    ret = []
    dfs(0,0,ret,nums,visited)
    return answer
    
 어떤 풀이로 접근 할까 생각했는데
다른 사람이 준 팁을 보고 문제의 답을 봤더니 ex) [3, 1, 2, 3] 중복을 제거했을때 배열에서 [1,2,3]에서 2개를 뽑았 어차피 2개만 다르게 되고 
[3,3,3,2,2,2] 일 경우 중복을 제거하면 [2,3] 이다. [3,3,3,2,2,2] 3개를 뽑으면 중복된 값이 있기에 서로다른 포켓몬의 개수는 최대 개수는 2가 된다. 이를 바탕으로
주어진 nums의 중복을 제거하고 그 길이가 뽑을 횟수 보다 크다면 뽑을 횟수는 정해저있기에 최대값은 뽑을 횟수이다. 작을 경우는 중복이 제거된 nums의 길이를 리턴하면 된다.
"""

def solution(nums):
    answer = 0
    deduplicationNums = set()
    for i in nums:
        deduplicationNums.add(i)

    if len(deduplicationNums) > len(nums)//2:
        return len(nums)//2
    
    return len(deduplicationNums)
    