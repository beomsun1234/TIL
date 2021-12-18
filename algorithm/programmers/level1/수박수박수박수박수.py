"""
level 1
연습문제 - 수박수박수박수박수박수?
"""
def solution(n):
    answer = ''
    if n == 1:
        return '수'
    if n ==2:
        return '수박'
    for i in range(n):
        if i% 2 ==0:
            answer+="수"
        else:
            answer+="박"
    return answer