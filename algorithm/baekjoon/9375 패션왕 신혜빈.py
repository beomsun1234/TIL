"""
9375 - 패션왕 신해빈

"""

t = int(input())

for i in range(t):
    n = int(input())
    wear = {}
    for i in range(n):
        c,category = input().split()
        if category not in wear:
            wear[category] = 1
        else:
            wear[category]+=1
    ret = 1
    for c in wear.values():
        ret*=(c+1)
    print(ret-1)
