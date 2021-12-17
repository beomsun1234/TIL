"""
level1 없는 숫자 더하기
"""
def solution(numbers):
    answer = 0
    for i in range(1,10):
        if i not in numbers:
            answer+=i
    return answer