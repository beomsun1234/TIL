## 중복 조합
n,m = map(int,input().split())
nums = list(map(int, input().split()))
nums.sort()
ret = []
def dfs(pick,idx):
    if pick == m:
        print(" ".join(map(str,ret)))
        return
    for i in range(idx,len(nums)):
        ret.append(nums[i])
        dfs(pick+1,i)
        ret.pop()
dfs(0,0)


## 중복 순열
n,m = map(int,input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False] * n
ret = []
def dfs(pick):
    if pick == m:
        print(" ".join(map(str,ret)))
        return
    for i in range(len(nums)):
        ret.append(nums[i])
        dfs(pick+1)
        ret.pop()
dfs(0)
