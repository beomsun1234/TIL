"""
2019 카카오 - 튜플
문제의 정답이 가장 많이 나온 숫자를 기준으로 위치해 있다는걸 알면 쉽게 풀수 있는 간단한 문제였다.  정규식을 이용하면 더 간단한 코드로 구현 가능 할 것 같다. 
print(re.findall('\d+',s)) 이렇게 숫자만 뽑을 수 있다

"""
def solution(s):
    answer = []
    s = s[1:-1]
    ret = []
    map = {}
    for i in range(len(s)):
        if s[i] == "{":
            idx = i + 1
            #괄호가 끝나는 idx를 찾는다
            while s[idx] != '}':
                idx+=1
            number = ""
            # 끝난 괄호에서 ,를 기준으로 숫자 값을 number에 기록한다. 
            for j in range(i+1,idx):
                if s[j]!=",":
                    number += s[j]
                else:
                    # ,면 기록한 number를 map에 넣어준다 
                    if number in map:
                        map[number] +=1
                    else:
                        map[number] = 1
                    # 사용한 number 초기화
                    number = ""
            # 마지막 숫자 넣어줌
            if number in map:
                map[number] +=1
            else:
                map[number] = 1
    
    #value를 기준으로 정렬
    map = sorted(map.items(), key = lambda x:x[1], reverse=True)
    for i in map:
        answer.append(int(i[0]))
    return answer
    