"""
백준 백트랙킹 연습
n과 m 8 - 15657

간단했다. 이문제는 중복을 포함하는 조합 문제이다.
"""

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
