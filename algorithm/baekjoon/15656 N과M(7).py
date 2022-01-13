"""
백준 백트랙킹 연습
n과 m 7 - 15656

간단했다. 이문제는 중복을 포함하는 순열 문제이다.
"""

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
