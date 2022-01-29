"""
5430 AC

아래는 처음 코드이다. 쉽게생각해서 시간 초과가 발생했다... 

처음 생각했던대로 짝수면 그대로 홀수면 뒤집는걸 적용해서 문제를 푸니 성공했다.. 즉 연산자가 D일 경우 deque를 사용하여 짝수면 앞을 제거하고 홀수면 뒤를 제거해주었다



# RR 이 두번오면 그대로 짝수면 그대로이다.
# D가
import sys
input = sys.stdin.readline

T = int(input())

# 수행할 함수
for i in range(T):
    p = input()
    n = int(input())
    data = input()
    nums = data[1:-2].split(",")
    if n == 0:
        nums = []
    flag = 0
    if p.count("D") > len(nums):
        print("error")
    elif p.count("D") > 0 and nums[0] == '':
        print("error")
    else:
        for op in p:
            if op == "R": # 뒤집기
                nums = nums[::-1]
            elif op == "D":
                if not nums:
                    flag = 1
                    break
                else:
                    nums.pop(0)
        if flag ==1:
            print("error")
        else:
            print("["+",".join(nums)+"]")
"""
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

# 수행할 함수
for i in range(T):
    p = input()
    n = int(input())
    data = input()
    nums = data[1:-2].split(",")
    if n == 0:
        nums = []
    q = deque(nums)
    if p.count("D") > len(nums):
        print("error")
    elif p.count("D") > 0 and nums[0] == '':
        print("error")
    else:
        flag = 0
        r_cnt = 0
        for op in p:
            if op == "R": # 뒤집기
                r_cnt +=1
            elif op == "D":
                if not q:
                    flag = 1
                    break
                else:
                    if r_cnt %2 == 0: ## R의 현재 수가 짝수면 그대로이므로 nums의 앞을 빼주면된다.
                        q.popleft()
                    else: 
                        q.pop()
        if flag ==1:
            print("error")
        else:
            if r_cnt % 2 == 0:
                print("[" + ",".join(q) + "]")
            else:
                q.reverse()
                print("["+",".join(q)+"]")