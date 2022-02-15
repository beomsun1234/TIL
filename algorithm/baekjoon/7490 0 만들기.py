"""

7490 - 0 만들기

간단했다. 오름차순 수열 1~N이 있을 때  +,-,'' 3가지 연산자를 숫자들 사이에 삽입하여 만든 수식의
결과 0이 되는 식을 찾는 문제이다. 연산자 3개를 N-1개 뽑고 백트랙킹을 이용해서 해당 식이 0인지 확인 하면 되는 문제이다.

'' 연산자는 숫자를 이어붙이면 된다.
"""


import re

T = int(input())

for i in range(T):
# + or - or ' '
    N = int(input())
    ret = []
    answer = []

    def convertAnswer(op):
        tmp = ''
        for idx,o in enumerate(op):
            if o == 0:
                data = idx+1
                tmp += str(data) + '+'
            elif o == 1:
                data = idx+1
                tmp += str(data)+  '-'
            elif o == 2:
                data = idx+1
                tmp += str(data) + " "
        tmp += str(N)
        return tmp


    def is_zero(exp):
        numbers = re.findall(r'\d+', exp)
        op = re.findall(r'\D+', exp)
        sum_val = int(numbers[0])
        for idx, o  in enumerate(op):
            if o == '+':
                sum_val += int(numbers[idx+1])
            if o == '-':
                sum_val -= int(numbers[idx+1])
        if sum_val == 0:
            return True
        return False
    def exp(op):
        tmp = ''
        for idx,o in enumerate(op):
            if o == 0:
                data = idx+1
                tmp += str(data) + '+'
            elif o == 1:
                data = idx+1
                tmp += str(data)+  '-'
            elif o == 2:
                data = idx+1
                tmp += str(data)
        tmp += str(N)
        return is_zero(tmp)

    def dfs(pick):
        if pick == N-1:
            if exp(ret):
                answer.append(convertAnswer(ret))
            return
        for i in range(3):
            ret.append(i)
            dfs(pick+1)
            ret.pop()
    dfs(0)

    answer.sort()
    for i in answer:
        print(i)
    print("")
    