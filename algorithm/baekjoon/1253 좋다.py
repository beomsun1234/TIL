
N = int(input())

n = list(map(int,input().split()))

n.sort()

start = 0
end = 1
cnt = 0

# 있으먄 end +=1
# 없으면 start+1
ans = 0
for i in range(N):
    tmp = n[:i] + n[i+1:]
    v =  n[i]
    start = 0
    end   = len(tmp) -1
    cnt = 0
    while start < end:
        v1 = tmp[start] + tmp[end]
        if v == v1:
            cnt+=1
            break
        if v1 < v:
            start +=1
        else:
            end -=1
    if cnt > 0:
        ans+=1
print(ans)
