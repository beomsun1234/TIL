from collections import  deque
def solution(edges):
    answer = [0,0,0,0]
    
    ## 생성된 정점은 찾기 정말정말 쉽다.
    ## edges-> [a,b] -> a에서 b로  a가 가장 많은 숫자가 정점
    edges_db = {}
    conn_info = {} # key =a , val = b
    start_edges = []
    edge = 0
    ##----정점 계산-----------------------
    for a,b in edges:
        if a not in edges_db:
            edges_db[a] =1
        else:
            edges_db[a] +=1
        # 연결정보 저장
        if a not in conn_info:
            conn_info[a] = [b]
        else:
            conn_info[a].append(b)
    max_val =  0
    for a,b in edges:
        conn = edges_db[a]
        if max_val < conn:
            max_val = conn
            edge = a
    answer[0]= edge
    ##---------------------------------
    ## 정점을 찾았으면 정점과 연결된 시작점을 저장한다.
    for i in conn_info[edge]:
        start_edges.append(i)
    ## 도넛모양은 n개의 정점과 n개의 간선이있고 시작점으로 돌아온다.
    ## 막대는 다시 돌아오지 않는다.
    ## 8자는 다시돌아오고 정점 + 1개 이다.
    visited = [0] * 1000001
    for start_edge in start_edges:
        cnt = 0 # 간선 
        e_cnt = 0 # 정점
        q = deque()
        q.append(start_edge)
        while q:        
            e = q.popleft()
            e_cnt +=1
            if visited[e] > 0:
                visited[e] -=1
            else:  
                visited[e] +=1
            if e in conn_info:
                for ee in conn_info[e]:
                    cnt +=1
                    if visited[ee] == 0:
                        q.append(ee)  
        if cnt - e_cnt == 1: # 8자
            answer[3] +=1
        elif cnt - e_cnt < 0: # 막대
            answer[2] +=1
        elif cnt - e_cnt == 0: #도넛
            answer[1] +=1
    ##  정점, 도넛 모양 , 막대 모양, 8자 모양 순서
    return answer
