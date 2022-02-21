"""
1966 - 프린터 큐
간단했다. 주어진 대로 구현하면 됐다.
"""
t = int(input())
for _ in range(t):
    N , M = map(int,input().split())
    data = list(map(int,input().split()))
    q = []
    # 큐에 우선순위와 인덱스를 튜플형태로 넣는다.
    for i in range(N):
        q.append((data[i],i))
    # 삭제했는지 체크 삭제 하지마 않았다면 flag = 0이며 우선순위가 높다는 뜻이다.
    flag = 0
    # 우선순위에 따라 배열에 저장
    ret = []
    # 몇번째에 출력됐는지 확인
    time = 0
    # 종료 조건은 최대 N개 만큼 출력 될 수 있으므로 
    while time <N:
        # 큐 앞의 우선순위를 기준으로 뒤에 우선순위들과 비교
        for i in range(1,len(q)):
            # 기준이 되는 우선순위보다 큰게 있다면 
            if q[0][0] < q[i][0]:
                # 현재 기준이 되는 우선순위는 뒤로간다.
                tmp = q.pop(0)
                q.append(tmp)
                flag = 1
                break
        # 현재 기준이 되는 우선순위가 가장 큰값이라면
        if flag == 0:
            time +=1
            # 큐에서 뺀다
            p = q.pop(0)
            # 만약 큐에서 뺀 값이 찾는 인덱스와 같은 거라면
            if p[1] == M:
                print(time)
                break
        flag = 0
        
