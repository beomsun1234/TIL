"""
1541- 잃어버린 괄호
쉽게 풀었다. 제출할때 디버그용 print를 지워야했는데 안지워서 오류나서 진짜 어휴.. 암튼 주의해야겠다..

로직은 간단했다. 숫자와 +,-로 분리한 후 숫자배열 0번째 값을 초기 값으로 설정하고 
연산자가 -일 경우 -가 나올때까지 반복문을 돌면서 tmpNum에 -시작 지점의 값부터 -가 나오기 전까지의 값을 넣어주고 tmpNum을 ret 변수에 -한 후 더해준 이후 
index를 교체해준다. 만약 + 일 경우 현재 인덱스 값을 더하면 된다. 

ex) 55-50+40
idx = 0 , op = '-' -> -가 나올때까지 반복문 돌리고 종료는 op배엷의길이보다 인덱스가 크거나 같으면 종료
- 는 0번인덱스고 50은 1번 인덱스이므로 숫자는 op배열인덱스의 +1이된다. (tmp = idx+1)

인덱스가 = 2 이 되면서 반복문을 탈출한다. 


"""


import re
# +,-, 숫자 배열 만든다.


s = input()
nums = re.findall("\d+", s)
op = re.findall("\+|-", s)

ret = int(nums[0])
idx = 0
while idx < len(op):
    if op[idx] == '-':
        tmp = idx+1
        tmpNum = int(nums[tmp])
        while tmp < len(op) and op[tmp] == "+":
            tmp+=1
            tmpNum += int(nums[tmp])
        ret += -tmpNum
        idx = tmp
    else:
        idx+=1
        ret += int(nums[idx]) 
    
print(ret)
