"""
카카오 2019  후보키
파이썬은 조합을 만들어주는 함수가 있다..
조합 combinations -> combinations(items, i)  조합을 만들려는 아이템과 조합의 수를 반드시넘겨줘야한다.

처음 접근은 dfs를 통해 각 컬럼의 조합을 뽑았다. ex) 이름, 학번, 주소, 지도교수 의 relation이 있다고 치면 {이름}, {이름,학번}, {이름,주소} .. 등의 조합을 뽑았다.
뽑은 컬럼의 조합을 가지고 주어진 relation의 각로우에 컬럼 값을 확인하여 같은 것이 있으면 유일성을 만족하지 않으므로 유일성을 만족하는 컬럼 조합을 찾는다. 이 다음에 엄청 삽질했다.. 처음 접근은 유니크한 것을 찾아서 후보키에 존재하지 해당 유니크값이랑 1개라도 같으면 flag를 줘서 후보키에 넣어주지 않았고, 해당 유니크한 키가 후보키에 없다면 (flag = 0) 후보키 카운트를 증가해주고 후보키에 배열에 넣어줬다. 이런식으로 할 경우 83점이 맞는다. 18, 19, 20, 25, 28가 실패한다. ex) [["a", "1", "aaa", "c", "ng"], ["b", "1", "bbb", "c", "g"], ["c", "1", "aaa", "d", "ng"], ["d", "2", "bbb", "d", "ng"]]이 케이스가 주어질 경우
(0), (2,3), (1,3,4)가 정답이지만 내가 전에 작성한 코드는 (0), (2,3)을 반환한다.. 당연하다 하나라도 같으면 후보키가 될 수 없으니 (2,3)에 3이 있고 (1,3,4)에 3이 있으니 1,3,4는 후보키에 들어올 수 없다. 해결 방법을 찾지 못해서 다른분의 풀이를 보고 풀 수 있었다... 미련하게 너무 오래 잡고 있었다...
최소성을 검사하는 아이디어는 유일성을 검사하고 나온 튜플 set들을 후보키 set의 부분집합인지 찾는 메소드인 issubset()을 사용해서 아닌 경우들만 unique 리스트에 넣었다
##알게 된점
discard(값) - 전달받은 값을 삭제 (없을 때 그냥 무시)
>>> k = {1, 2, 3}
>>> k.discard(3)
>>> k
{1, 2}

isdisjoint() - 두 집합이 공통 원소를 갖지 않는가?
------
issubset() - 부분집합(subset)인가?
ex)
>>> a = {1, 2, 3, 4, 5}
>>> b = {1, 2, 3}
>>> a.issubset(b)
False
>>> b.issubset(a)
True
----
조합 combinations

combinations(items, i) # 조합을 만들려는 아이템과 조합의 수를 반드시넘겨줘야한다.




-------

#후보키 얻기
def getCandidateKey(ret,combi,relation,row,key):
    check = set()
    global cnt
    ret = []
    a = ""
    flag = len(combi[0])-1
    for c in combi:
        for i in range(row):
            for col in c:
                a += relation[i][col]
                if flag > 0:
                    a+="."
                flag -=1
            flag = len(combi[0])-1
            check.add(a)
            a = ""
        if len(check) == row: # 유니크한 경우
            f = 0
            
            for i in key: #후보키들과 현재 유니크한 col 비교하여 같은게 있으면 최소성 x
                for z in i:
                    for j in c:
                        if j in z:
                            f +=1
            if f ==0: # 최소성 만족
                ret.append(c)
                cnt+=1
        check = set()
    return ret
def dfs(pick,ret,idx,size,col,visited,combination): # 컬럼 조합
    if pick == size+1:
        combination.append(ret[:])
        return
    for i in range(idx,col):
        if not visited[i]:
            visited[i] = True
            ret.append(i)
            dfs(pick+1,ret,i,size,col, visited,combination)
            ret.pop()
            visited[i] = False
from itertools import combinations
def solution(relation):
    row = len(relation)
    col = len(relation[0])
    answer = 0
    ret = []
    key = []
    c = []
    global cnt
    cnt = 0 
    combination = []
    visited = [False] * col
    # dfs(pick,ret,idx,size,col,visited,combination):
    for i in range(0,col):
        dfs(0,ret,0,i,col,visited,combination)
        visited = [False] * col
        c.append(getCandidateKey(key,combination,relation,row,c))
        combination = []
        ret = []
    print(c)
    return cnt
"""
from itertools import combinations
def solution(relation):
    answer = 0
    rows = len(relation)
    cols = len(relation[0])
    candidateKeys = []
    comRows = []
    combinationCols = []
    for i in range(1, cols+1):
        combinationCols.extend(combinations(range(cols),i))
    for combi in combinationCols:
        checkRows = []
        for item in relation:
            c = "" # 각 컬럼값을 합쳐서 row를 만든다
            for idx in combi:
                c+=item[idx]
            checkRows.append(c)
        comRows = tuple(checkRows) # 로우 완성
        if len(set(comRows)) == rows: # 완성된 각 로우가 중복되는게 있는지 체크
            flag = True
            for candidateKey in candidateKeys:
                if set(candidateKey).issubset(set(combi)): #동일한 요소를 가지고 있는지 검사(유일성을 통과한 combi에 후보키의 부분집합이 있는지 체크)
                    flag = False
                    break
            if flag:
                candidateKeys.append(combi)
    
    print(candidateKeys)
    return len(candidateKeys)