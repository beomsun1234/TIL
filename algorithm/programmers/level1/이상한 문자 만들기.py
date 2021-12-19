"""
이상한 문자 만들기- level 1 

split함수를 사용할줄 몰라서 직접 공백을 기준으로 각 단어들을 만들어 주었다.... 
split 함수를 사용하니 코드가 반 이상이나 줄었다.. 


string.lower()
string.upper()
string.split(" ") -> split함수에 인자로 공백을 넣을시 양쪽에 공백을 제거하여 반환해준다
"""
def solution(s):
    answer = ''
    print(s.count(" "))
    ## 단어의 개수는 공백의 개수에 +1 한 값
    words = [""] * (s.count(" ")+1)
    cur = 0
    index = 0
    ## 공백을 기준으로 단어 나누기
    for idx,c in enumerate(s):
        if c == " ":
            for i in range(cur,idx):
                words[index]+=s[i]
            cur = idx+1
            index+=1
        if idx == len(s)-1:
            for i in range(cur,len(s)):
                words[-1]+=s[i]
    
    # 나눈 단어의 문자열 중 인덱스가 짝수면 대문자로 치환 홀수면 소문자로 치환
    for i in range(len(words)):
        for j in range(len(words[i])):
            if j% 2==0:
                answer+= words[i][j].upper()
            else:
                answer+=words[i][j].lower()
        if i < len(words)-1:
            answer+=" "
    return answer
    
## 수정 코드
def solution(s):
    answer = ''
    words = s.split(" ")
    for i in range(len(words)):
        for j in range(len(words[i])):
            if j % 2 == 0:
                answer+=words[i][j].upper()
            else:
                answer+=words[i][j].lower()
        answer+=" "
    return answer[:-1]
    
