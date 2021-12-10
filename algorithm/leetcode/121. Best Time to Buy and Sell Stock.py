"""
    leetcode
    121. Best Time to Buy and Sell Stock
    파악한게 -> 뒤로 돌아갈 수 없다. 날짜 중 가장 작은 값을 선택하고 날짜 중 가장 큰(선택한 날짜 이후) 값을 가져와 더하면 될 것같다. 
    edge case - 7 6 4 3 1 만약 값이 내림차순으로 정렬한 값이랑 주어진 prices 두개가 같으면 return
    //--- 시간초과(완전탐색)
    def maxProfit(self, prices: List[int]) -> int:
        maxV = -10000
        minV = prices[0]
        for nowDay,price in enumerate(prices):
            for afterDay in range(nowDay+1,len(prices)):
                maxV = max(maxV, prices[afterDay]-prices[nowDay]) 
        
        if maxV < 0:
            return 0
        return maxV
        
    ## 그리디로 풀면
    우선 최소값을 prices의 0번째 값으로 둔 후 날이 지날때마다 이전에 고른 최소값이 현재 값보다 작음면 최소값을 갱신해 주면서 우리가 현재 주식 가격에서 최소값을 뺀 값을 맥스와 비교해서 같으면 리턴
"""
from typing import List


def maxProfit(self, prices: List[int]) -> int:
    maxV = -10000
    minV = prices[0]
    for day in range(len(prices)):
        minV = min(minV, prices[day])
        print(minV,prices[day])
        maxV = max(maxV, prices[day]-minV)
        print(maxV,prices[day]-minV)
        
    return maxV
        
