"""
프로그래머스 level2- 최대값과 최솟값

"""
def solution(s):
    answer = ''
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = int(s[i])
    answer += str(min(s))
    answer += " "
    answer += str(max(s))
    return answer
    