"""
백준 2110번 공유기 설치

기준을 성공적을 잡았지만 기준거리를 사용해서 두 집 사이의 거리를 체크하는 부분에서 잘 못 접근해서 4%에서 자꾸 실패했다..
공유기를 설치하는 것을 생각하지 않았다... 공유기 설치 로직은 공유기 설치시 가능한 최대 기준 거리를 mid로 정하고(left+right/2) 공유기 설치 좌표를 1번인덱스에 있는 집으로 초기화하고
해당 공유기 설치 위치에서 다음 공유기를 설치한 집까지의 거리가 mid보다 클 경우만 설치하면 된다. 만약 공유기를 C개 이상 설치 할 수 있다면 최솟값과 정답을 갱신해주고, 만약 C개 미만으로 설치했다면 최대값을 갱신해준다.

"""

N, C = map(int,input().split())
route = []
for i in range(N):
    data = int(input())
    route.append(data)
route.sort()
answer = 0
# 설치한 공유기 사이의 거리 최솟값 
left =1

# 최대값
right = route[-1] - route[0]

while left <= right:
    # 기준이되는 설치한 공유기 사이의 거리
    mid = (left+right)//2
    # 가장 처음집에 하나 설치 
    installed_route = route[0]
    ## 공유기 개수
    router_cnt = 1
    for i in range(N):
        if route[i] - installed_route >=  mid:
            router_cnt +=1
            installed_route = route[i]
    if router_cnt >= C:
        answer = mid
        left = mid +1
        continue
    right = mid -1
    

print(answer)