"""
14889 스타트와 링크

dfs를 사용해서 조합으로 n / 2 명의 사람을 선택해 팀을 나눈다
select에 저장된 수가 0 혹은 1인지에 따라 팀을 구분할 수 있다
"""

import sys
input = sys.stdin.readline
def dfs(idx, cnt):
    global ans
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if select[i] and select[j]:
                    start += a[i][j]
                elif not select[i] and not select[j]:
                    link += a[i][j]
        ans = min(ans, abs(start - link))

    for i in range(idx, n):
        if select[i]:
            continue
        select[i] = 1
        dfs(i + 1, cnt + 1)  #cnt= pick 횟수
        select[i] = 0


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

select = [0 for _ in range(n)]
ans = sys.maxsize
dfs(0, 0)
print(ans)
