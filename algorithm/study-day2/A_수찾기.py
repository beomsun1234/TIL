def b_s(arr,start, end, num):
    if start > end:
        print(0)
        return 0

    mid = (start+ end)//2
    if arr[mid] == num:
        print(1)
        return 1
    elif arr[mid] > num:
        return b_s(arr, start, mid-1, num)
    else:
        return b_s(arr, mid+1, end, num)
    
    
n = int(input())
arr_n = list(map(int, input().split())) 
arr_n.sort()
m = int(input())
arr_m = list(map(int, input().split()))

for i in range(m):
    b_s(arr_n,0,n-1, arr_m[i])


## 한번 틀렸다.... 이유는 end를 n으로 하니 실패했다....