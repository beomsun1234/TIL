"""
백준 3020 - 개똥벌레
"""
N, H = map(int,input().split())
cave = []
up = []
down = []
# 장애물이 짝수는 아래에서, 홀수는 위에서 내려옴 
for i in range(N):
    data = int(input())
    #짝수면 아래
    if i %2==0:
        down.append(data)
    else:
        up.append(data)

up.sort()
down.sort()
def binarySearch(array,h):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left + right) //2
        #가장 적게 부수는거 찾기
        if h < array[mid]:
            right = mid -1
            continue
        left = mid +1
    return len(array) - left  

d_cnt = 0
u_cnt = 0
min_destory_cnt = N
section_cnt = 0
for h in range(1,H+1):
    d_cnt = binarySearch(down,h-1)
    u_cnt = binarySearch(up,H-h)
    destory_cnt = d_cnt+ u_cnt
    if min_destory_cnt > destory_cnt:
        min_destory_cnt = destory_cnt
        section_cnt = 1
    elif min_destory_cnt == destory_cnt:
        section_cnt +=1
print(min_destory_cnt, section_cnt)
 