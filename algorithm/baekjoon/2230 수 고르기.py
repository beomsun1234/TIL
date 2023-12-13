N, M = map(int,input().split())

n = []

for i in range(N):
    val = int(input())
    n.append(val)

n.sort()


start = 0
end = 0

minVal = 2000000000
while start < N and end < N:
    c = n[end] - n[start] 
    if c >= M:
        minVal = min(minVal,c)
        start +=1
    else :
        end +=1


print(minVal)
