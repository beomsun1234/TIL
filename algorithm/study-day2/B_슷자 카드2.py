from bisect import bisect_left, bisect_right

n = int(input())
arr_n = list(map(int, input().split())) 
arr_n.sort()
m = int(input())
arr_m = list(map(int, input().split()))

for i in range(m):
    idx1 = bisect_left(arr_n, arr_m[i])
    idx2 = bisect_right(arr_n, arr_m[i])
    print(idx2-idx1)