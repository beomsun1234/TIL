"""
2407 조합
ex) 5c3 

5x4x3 / 3x2x1

"""


n, m = map(int, input().split())
answer = 1
k = n - m

while n > k:
    answer *= n
    n -= 1
while m > 1:
    answer = answer // m
    m -= 1

print(answer)