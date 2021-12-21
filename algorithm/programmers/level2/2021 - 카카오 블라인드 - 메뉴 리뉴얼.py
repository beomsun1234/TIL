"""
level 2 메뉴 리뉴얼

시간 초과를 생각안하고 푸는거면 쉬운 것 같았다.. 초과 생각안하고 제출하니 역시 10 이후 테스트케이스는 런타임 에러가 났다.. 밑에는 처음 제출한 코드이다..
주어진 orders에서 중복되는 알파벳을 가지고 조합을 만든 후 딕셔너리에 키를 해당 조합이 orders와 일치하는 개수를 넣어 주었다. value로는 조합한 알파벳이다. 각 course에 해당하는 조합을 뽑고 나서 가장 큰 값만 answer에 저장해주는 방법으로 접근했다.. max값을 찾는데에서도 시간이 많이 소비된것 같았다.. 다른 접근 방법으로 
각 order의 메뉴들을 조합하고 조합한 메뉴가 몇개가 나오는지 확인하여, 딕셔너리를 구성(key=문자조합, values = count) 2개 이상이고 가장큰 값을 answer에 담아 return 해주면 됐다.

def dfs(pick, idx, test,visited,ret,orders,size, answer,tt):
    global maxVal
    if pick == size:
        ## 두개 이상 주문 할 경우 세트구성
        cnt = 0
        tmp = 0
        for i in orders:
            for j in ret:
                if i.count(j) == 1:
                    cnt+=1
            if cnt == size:
                tmp +=1
            cnt = 0
        if tmp >=2:
            maxVal = max(maxVal, tmp)
            if tmp in tt.keys():
                tt[tmp].append(ret.copy())
            else:
                tt[tmp] = [ret.copy()]
        return
    for i in range(idx,len(test)):
        if not visited[i]:
            visited[i] = True
            ret.append(test[i])
            dfs(pick+1, i,test,visited,ret,orders,size,answer,tt)
            ret.pop()
            visited[i] = False

def solution(orders, course):
    answer = []
    ret = []
    test = set()
    global candidates
    global maxVal
    maxVal = 0
    tt = {}
    for i in orders:
        for j in i:
            test.add(j)
    dupl = sorted(test)
    visited = [False] * 11
    pp = []
    for j in course:
        if j <= len(orders):
            dfs(0, 0, dupl,visited,ret,orders,j,answer,tt)
            if maxVal in tt:
                for i in tt.get(maxVal):
                    pp.append("".join(i))
            tt = {}
            maxVal = 0
            visited = [False] * 11
    pp.sort()
    return pp
"""
def dfs(pick, idx, test,visited,ret,orders,size, answer,candidates):
    global maxVal
    if pick == size: ## course 만큼 뽑는다
        candidates.append(ret.copy())
        return 
    for i in range(idx,len(test)):
        if not visited[i]:
            visited[i] = True
            ret.append(test[i])
            dfs(pick+1, i,test,visited,ret,orders,size,answer,candidates)
            ret.pop()
            visited[i] = False

def solution(orders, course):
    answer = []
    visited = [False] * 26
    ret = []
    map = {}
    deduplCourseCombi = set()
    for cc in course:
        map = {}
        for i in orders:
            candidates = []
            ## 주어진 orders의 각 메뉴로 조합을 만든다.
            dfs(0,0,sorted(i),visited,ret,orders,cc,answer,candidates)
            
            #만들어진 조합이 몇개가 나왔는지 확인
            for c in candidates:
                candidate = "".join(c)
                if candidate in map:
                    map[candidate] +=1
                else: 
                    #자기 자신만있을경우 =1
                    map[candidate] = 1
        if len(map) == 0: ## map에 아무 것도 없으면 넘어감
            continue
        if max(map.values()) >=2: ## 두개 이상 주문 할 경우 세트구성
            for key, value in map.items():
                if max(map.values()) == value:
                    deduplCourseCombi.add(key)
    answer = sorted(deduplCourseCombi)
    return answer
    