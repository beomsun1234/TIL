"""
백준 - 2343 기타레슨
"""
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
lecture=list(map(int,input().split()))
left=max(lecture)
right=sum(lecture)
ans=sys.maxsize
while left<=right:
    mid=(left+right)//2
    cnt=0
    tmp=0
    for i in range(N):
        if tmp+lecture[i]>mid:
            cnt+=1
            tmp=0
        tmp+=lecture[i]
    print(tmp, mid, cnt)
    #블루레이의 크기를 구한 후 현재 블루레의 값이 0이 아니면 하나 더 있다는 뜻이므로 하나 추가해준다.
    if tmp >0:
        cnt+=1
    # 만들수 있는 블루레이의 수가 M보다 크면 블루레이의 최솟값을 수정
    if cnt>M: 
        left=mid+1
        continue
    # 아니면 최대값을 수정
    ans=min(ans,mid)
    right=mid-1
print(ans)

 