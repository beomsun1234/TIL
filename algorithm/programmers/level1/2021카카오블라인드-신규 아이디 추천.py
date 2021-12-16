"""
level 1 신규아이디추천
아이디의 길이는 3자 이상 15자 이하여야 합니다.
아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

문제는 쉬운데 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다. 여기 부분에서 살짝 고민했다.. 어떤식을 치환 할까 생각했다. 여러 고민끝에 방법이 떠오르지 않았다.. 힌트를 얻고 해결 할 수 있었다. 아이디어는 '..' 이렇게 마침표가 2일 경우를 찾아서 하나로 치환해주었다 
나머지는 너무 간단했다
# 알게된 점
string.lower() string 객체 내의 모든 문자를 소문자로 변환하여 리턴

string.isalnum() 문자열이 모두 숫자일 경우 true 리턴

string.isalpha() 문자열이 모두 한글이나 영어일 경우 true 리턴

String.replace("찾을값", "바꿀값", [바꿀횟수])

"""
def changeId(new_id):
    answer = ""
    ## 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()
    tmp = []
    ## 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    for i in new_id:
        if i == '-' or i == '_' or i == '.' or i.isalpha() or i.isalnum():  
            tmp.append(i)
    answer = "".join(tmp)
    ## 3단계  new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다
    while '..' in answer:
        answer = answer.replace('..','.')
    ## 4단계 처음이나 끝에 위치한다면 제거합니다.
    if answer[0] == '.':
        if len(answer) > 1:
            answer = answer[1:]

    if answer[-1] == '.':
        answer = answer[:-1]
    
    ## 5단계 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if answer == "":
        answer+='a'
    ## 6단계  new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다. 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(answer) >=16:
        answer = answer[0:15]
    if answer[-1] == '.':
        answer = answer[:-1]
        
    ## 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(answer) <=2:
        count = 3 - len(answer)
        print(answer[len(answer)-1])
        while count >0:
            answer += answer[len(answer)-1]
            count -=1

    return answer

def solution(new_id):
    answer = ''
    return changeId(new_id)
    