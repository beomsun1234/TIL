"""
백준 백트랙킹 연습
n과 m 9 - 15663

간단했다. 중복되는 수열을 여러 번 출력하면 안되는 순열 문제이다.
뽑고나서 check set을 확인해서 뽑은 값이 check에 존재하면 중복되는 것이므로 return 아니면 print후 check에 뽑은 값을 넣어준다.
"""
n,m = map(int,input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False] * n
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
        if not visited[i]:
            visited[i] = True
            ret.append(nums[i])
            dfs(pick+1)
            ret.pop()
            visited[i] = False
dfs(0)
