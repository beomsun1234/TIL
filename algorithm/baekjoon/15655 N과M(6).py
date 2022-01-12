"""
백준 n과m 6 15655번

이건 조합 문제이다. 쉽게 풀 수 있었다. n과m 5와 같지만 5는 순열이고 이 문제는 조합이다
"""
n, m = map(int, input().split())
nums = list(map(int,input().split()))
nums.sort()
ret = []
## 조합
def dfs(pick, idx):
    if pick== m:
        print(" ".join(map(str,ret)))
        return
    for i in range(idx, len(nums)):
        ret.append(nums[i])
        dfs(pick+1, i+1)
        ret.pop()

dfs(0,0)