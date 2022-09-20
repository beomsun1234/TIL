"""
두 큐 합 같게 만들기

"""

def solution(queue1, queue2):
    nums = queue1+queue2
    target = sum(nums)/2 
    
    answer = 0
    s = 0
    e = len(queue1)
    interval_sum = sum(queue1)
    
   
  
    while (answer<len(queue1)*5 and e < len(nums)):
        
        if interval_sum == target:
            return answer
        
        elif interval_sum > target:
            interval_sum -= nums[s] 
            s+=1
        else:
            interval_sum += nums[e]
            e+=1
        answer +=1
            
    return -1
