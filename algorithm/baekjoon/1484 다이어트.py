G = int(input())

#a** - b ** = G
nowW = 1
reW = 1

ans = []

for i in range(0, 100000):
    nW = nowW * nowW
    rW = reW * reW
    g = nW - rW 
    if g == G:
        print(nowW)
        ans.append(nowW)
    if g > G:
        reW +=1
    elif g<=G:
        nowW +=1
    

if len(ans) == 0:
    print(-1)
