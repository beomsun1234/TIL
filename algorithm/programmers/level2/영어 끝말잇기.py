"""

level2 - Summer/Winter Coding(~2018) - 영어 끝말잇기

간단하게 풀 수 있었다. 찾은 인덱스를 바탕으로 번호와 차례를 뽑아내는데 조금 헷갈렸지만 바로 풀 수 있었다.


"""
def solution(n, words):
    answer = []
    size = len(words)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    idx = 0
    # 스택을 만들고 처음 단어를 넣어주고 words에서 제거해준다.
    stack = []
    stack.append(words[0])
    words.pop(0)
    
    #끝말잇기를 모두 성공할 경우 0
    flag = 0
    while 1:
        idx+=1 # 현재 단어의 인덱스 
        if not words: # 단어를 모두 사용했으면 종료
            break
        word1 = stack[-1] #스택에 단어
        word2 = words[0] # 현재 단어
        
        # 스택에 맨 위에 있는 단어의 마지막 값과 현재 단어 첫번째 값이 일치해야한다.
        if word1[-1] != word2[0]: 
            flag = 1 # 끝말잇기를 완수하지 못했으므로 flag = 1
            break # 종료
        # 스택에 해당 단어가 있으면
        if word2 in stack: 
            flag = 1 # 종료
            break
        # 조건에 만족하면 
        # 스택에 현재 단어를 넣는다
        stack.append(word2)
        # 현재 단어를 사용했으므로 words에서 빼낸다
        words.pop(0)
    if flag == 0: #탐색 이후 flag가 0이면 모두 성공 [0,0] 리턴
        return [0,0]
    # 걸린사람의 번호는 찾은 인덱스 idx를 n으로 나눈 나머지에 0번 인덱스에서 시작하므로 +1 해준다.
    # 차례는 걸린사람의 idx를 n으로 나눈 몫의 값에 +1해주면된다.
    return [idx%n + 1, idx//n +1]