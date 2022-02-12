"""

1149 r,g,b 거리

   i  j             i
db[0][0], [1] ,[2]  0 -> 1번집
db[1][0], [1] ,[2]  1 -> 2번집
db[2][0], [1] ,[2]  2 -> 2번집 

 j= 0 -> r , 1-> g , 2-> b


만약 i번집이 red를 사용할 경우 i-1번집은 blue, green 이어야한다.

elseif i번집이 blue를 사용 할 경우 i-1번집은 red, green 이어야한다.

elseif i번집이 green을 사용 할 경우 i-1번집은 red, blue를 사용해야한다.

"""
N = int(input())

dp = [[0]*3 for _ in range(N)]

# dp테이블 셋팅
for i in range(N):
   data = list(map(int,input().split()))
   dp[i][0] = data[0]
   dp[i][1] = data[1]
   dp[i][2] = data[2]
   

#비교
for i in range(1,N):
   ## red선택시
   # blue, green의 최솟값 더해줌
   dp[i][0] += min(dp[i-1][1],dp[i-1][2])
   ## green선택시
   dp[i][1] += min(dp[i-1][0], dp[i-1][2])
   ## blue선택시
   dp[i][2] += min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1]))