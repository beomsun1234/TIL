N = int(input())
ret = []
arr_num = []

def convertArrToInt(arr):
    ret = ''
    for i in arr:
        ret += str(i)
    return int(ret)



# pick = 자리수
def dfs(pick, N):
    if pick == 10:
        ret.append(convertArrToInt(arr_num))
        return
    ret.append(convertArrToInt(arr_num))
    for i in range(0, 9):
        if arr_num[-1]>i:
            arr_num.append(i)
            dfs(pick+1,N)
            arr_num.pop()

if N >= 1023:
    print(-1)
else:
    for i in range(0,10):
        arr_num = [i]
        dfs(1,N)
    ret.sort()
    print(ret[N])