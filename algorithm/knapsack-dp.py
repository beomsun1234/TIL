#### DP
"""
itmes =  [
    [465,100],
    [400,85],
    [255,55],
    [350,45],
    [650,130],
    [1000,190],
    [455,100],
    [100,25],
    [1200,190],
    [320,65],
    [750,100],
    [50,45],
    [550,65],
    [100,50],
    [600,70],
    [255,40]
]
items의 첫번째 값은 value, 두번재는 weight
cap = 200
res = [1505,[7,12,14,15]]


            items   cap
base case -> []  , 0

dpTable

cap             0 1 2 3 4 5 6 7 8 9 10
index 0 []      0 0 0 0 0 0 0 0 0 0 0
      1 [1,2]   0 0 1 1 1 1 1 1 1 1 1
      2 [4,3]   0 0 1 4 4 5 5 5 5 5 5   
      3 [5,6]   0 0 1 4 4 5 5 5 6 9 9   
      4 [6,7]   0 0 1 4 4 5 5 6 6 9 10  
                                             
cap = 10

  dp[i][c] = max(dp[i-1][c],dp[i-1][c-curW]+curV)
  
  output = [10,[1,3]]



"""

itmes =  [
    [465,100],
    [400,85],
    [255,55],
    [350,45],
    [650,130],
    [1000,190],
    [455,100],
    [100,25],
    [1200,190],
    [320,65],
    [750,100],
    [50,45],
    [550,65],
    [100,50],
    [600,70],
    [255,40]
]

cap = 200

dp = []

# init dpTable
for i in range(0,len(itmes)+1):
    dp.append([])
    for j in range(0,cap+1):
        dp[i].append(0)

# apply formula
for i in range(1,len(itmes)+1):
    curValue = itmes[i-1][0]
    curWeight = itmes[i-1][1]
    for c in range(1,cap+1):
        if c < curWeight:
            dp[i][c] = dp[i-1][c]
        else:
            dp[i][c] = max(dp[i-1][c], dp[i-1][c-curWeight]+curValue)


curIndex = len(itmes)
w  = cap


print(dp[len(itmes)][cap])
