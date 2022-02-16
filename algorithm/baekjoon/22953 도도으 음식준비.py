"""
22953 도도의 음식준비

격려 조합을 뽑기 까지는 간단했지만 뽑고나서 시간 계산이 어려웠다.. 이분 탐색을 사용해서 뽑은 격려 조합을 뽑고 난 후 시간을 계산해 주어야한다.

"""

N, K , C = map(int,input().split())

work_times = list(map(int,input().split()))

global min_val
min_val = 1000000*1000000*100

# 격려 조합을 뽑고 나서 격려 한 후 시간 계산하기
def findTime(combi):
    global min_val
    tmp = work_times[:]
    for i in combi:
        tmp[i-1] -=1
        if tmp[i-1] == 0: # 1초 미만으로 줄 수없다.
            return
    left = 1
    right = 1000000*1000000*100
    while left <= right:
        mid = (left+right)//2
        cnt = 0
        for i in tmp:
            cnt+=mid//i
        if cnt >= K:
            min_val = min(min_val,mid)
            right = mid -1 
        else:
            left = mid +1
    return
# 격려 조합 뽑기 중복가능
combi = []
def dfs(pick,idx):
    if pick == C: ## 모두 격려 할 경우
        findTime(combi)
        return
    findTime(combi) # 한명 이상 격려 할 경우
    for i in range(idx,N+1):
        combi.append(i)
        dfs(pick+1,i)
        combi.pop()

dfs(0,1)
print(min_val)

