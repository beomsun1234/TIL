N, K= map(int, input().split())
tmp_pick_alphas = []

nam_words = []

global  answer
answer = 0


for i in range(N):
    nam_word = input()
    word_set = set()
    for w in nam_word:
        word_set.add(w)
    nam_words.append(word_set)

def addAlphaCombiToAlpha(combi_pick_alphas):
    alphas = {'a','c', 'i', 'n', 't'}
    if len(combi_pick_alphas) <1:
        return alphas
    for i in combi_pick_alphas:
        alphas.add(i)
    return alphas

def getReadCnt(combi_pick_alphas):
    alphas = addAlphaCombiToAlpha(combi_pick_alphas)
    ret = 0
    for i in range(N):
        is_read = True
        for w in nam_words[i]:
            if w not in alphas:
                is_read = False 
                break
        if is_read == True:
            ret+=1
    
    return ret

def dfs(pick,idx):
    global  answer
    if pick == K-5:
        # 검증 
        tmp = getReadCnt(tmp_pick_alphas)
        if answer <= tmp:
            answer = tmp
        return

    for i in range(idx,123):
        # a,n,tic는 제외
        if i not in (97,99,105,110,116):
            tmp_pick_alphas.append(chr(i))
            dfs(pick+1,i+1)
            tmp_pick_alphas.pop()

if K < 5:
    print(0)
elif K >= 26:
    print(N)
else:
    dfs(0, 97)
    print(answer)