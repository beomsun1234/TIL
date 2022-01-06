"""
프로그래머스 - level2 다음 큰 숫자

"""
def solution(n):
    answer = 0
    oneCnt = bin(n)[2:].count('1')
    while 1:
        n+=1
        binaryNumber = bin(n)[2:]
        if binaryNumber.count('1') == oneCnt:
            return n
    return answer
    
