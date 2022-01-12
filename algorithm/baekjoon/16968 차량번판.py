"""
백준 백트래ㅣㅇ 문제

16968 차량번호판
"""


def dfs(pick, pick_size, nowChr):
    global answer
    if pick_size == pick: ## 입력한 문자만큼 뽑는다
        answer+=1
        return
    if beonho[pick] == 'c': # 알파벳
        for i in range(26):
            if nowChr != chr(i+65):
                dfs(pick+1,pick_size, chr(i+65))
    elif beonho[pick] == 'd': #숫자
        for i in range(10):
            if nowChr != str(i):
                dfs(pick+1,pick_size, str(i))

## 문자 입력 인덱스로 한다.
beonho = input()
global answer
answer = 0
dfs(0,len(beonho),'')
print(answer)
