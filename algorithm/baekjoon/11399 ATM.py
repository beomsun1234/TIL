"""
11399 ATM
"""

N = int(input())

P = list(map(int, input().split()))
P.sort()
ret = 0
for i in range(1,N):
    ret += P[i] + sum(P[:i]) 
print(ret+P[0])