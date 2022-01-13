"""
백준 백트랙킹 연습
n과 m 11 - 15665

간단했다. 중복되는 수열을 여러 번 출력하면 안되는 중복순열 문제이다.
"""
## 중복 순열
n,m = map(int,input().split())
nums = list(map(int, input().split()))
nums.sort()
ret = []
check = set()
def dfs(pick):
    if pick == m:
        if " ".join(map(str,ret)) in check:
            return
        print(" ".join(map(str,ret)))
        check.add(" ".join(map(str,ret)))
        return
    for i in range(len(nums)):
        ret.append(nums[i])
        dfs(pick+1)
        ret.pop()
dfs(0)
