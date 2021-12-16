"""
level 1 숫자 문자열과 영단어
너무 간단했다.. 각 영어를 해당 숫자로 치환하고 만들어지 문자열을 int로 변환하면 끝

"""
def solution(s):
    answer = 0
    s = s.replace("zero",'0')
    s = s.replace("one",'1')
    s = s.replace("two",'2')
    s = s.replace("three",'3')
    s = s.replace("four",'4')
    s = s.replace("five",'5')
    s = s.replace("six",'6')
    s = s.replace("seven",'7')
    s = s.replace("eight",'8')
    s = s.replace("nine",'9')
    answer = int(s)
    return answer
    
