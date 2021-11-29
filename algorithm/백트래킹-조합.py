# 3c2
## 조합
result =[0]*2
n = [1,2,3]

r = 2##pick

def dfs(L,bw): # 뎊스와 다음시작점 표시
    print(bw)
    if L==r:
        print(result)
        return 
    else:
        for i in range(bw,len(n)):
            print(i)
            result[L]=n[i]
            dfs(L+1,i+1)


result = [0]*r
dfs(0,0)
