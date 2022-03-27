"""
백준 17140 - 이차원 배열과 연산 

빡 구현 느낌이다.. 간단하지만 한번 잘못 접근하면 골치 아프다... 우선 R연산과 C연산을 구분하는데 R 연산은 현재 row >= column 일 경우 진행하며,
C연산은 column>row 일 때 진행한다. 아래와 같이 배열이 주어질때 ROW >= column이므로 R연산을 진행해보면
1 2 1        (2,1), (1,2)             2 1 1 2          2 1 1 2 0 0
2 1 3   ->   (1,1), (2,1), (3,1)  ->  1 1 2 1 3 1 ->   1 1 2 1 3 1
3 3 3        (3,1)                    3 3              3 3 0 0 0 0

이 되며 크기가 가장 큰 행은 2번이고, 나머지 행의 뒤에 0을 붙여준다. 구해진 배열은 현재 row < column이므로 C연산을 진행한다.

2 1 1 2 0 0      | 1 |  | 3 |  | 1 |  | 1 |  | 3 |   | 1 |     1 3 1 1 3 1
1 1 2 1 3 1   -> | 1 |  | 1 |  | 1 |  | 1 |  | 1 |   | 1 | ->  1 1 1 1 1 1
3 3 0 0 0 0      | 2 |  | 0 |  | 2 |  | 2 |  | 0 |   | 0 |     2 1 2 2 0 0
                 | 1 |  | 0 |  | 1 |  | 1 |  | 0 |   | 0 |     1 2 1 1 0 0 
                 | 3 |  | 0 |  | 0 |  | 0 |  | 0 |   | 0 |     3 0 0 0 0 0
                 | 1 |, | 0 |, | 0 |, | 0 |, | 0 | , | 0 |     1 0 0 0 0 0

C연산 로직을 잘 못 접근해서 골치아팠다..  c연산로직은 우선 컬럼 기준으로 구해진 배열을 탐색하면 컬럼인덱스가 0일때 2,1,3이며 딕셔너리를 이용해서 해당 숫자가 몇번 나왔는지를 기록한고 나온 숫자의 개수를 기준으로 정렬하고 동일 할 경우 해당 숫자 크기를 기준으로 정렬한다. 
파이썬에서 딕셔너리를 정렬할 경우 리스트로 나온다. 해당 리스트는 (숫자, 횟수) 형식이며 컬럼을 기준으로 순서대로 숫자와 횟수를 tmp배열에 기록해 준다.
(2,1,3) ->  (1,1),(2,1),(3,1) 이 0번으로 설정하기 위해서는 tmp[r][0]에 넣어주면 된다. 리스트의 값 중 2개를 다 사용했다면 사용한 값의 리스트를 삭제해 준다(리스트 앞). 이렇게 반복하면서 가장 긴 row의 수를 찾는다(c연산은 컬럼이 변하지 아늠).
찾는 방식은 리스트의 길이 x2가 가장 큰 값을 찾으면 된다. 이후 A에 대입해주고 A는 row값은 설정한 tmp의 row값과 같게 된다. 즉 필요 없는 값들도 들어가게 된다. A를 가장긴 row만큼 잘라주고 리턴해주면 C연산을 수행한다.
"""
from collections import defaultdict
R,C, k = map(int,input().split())
A = []
for _ in range(3):
    data = list(map(int,input().split()))
    A.append(data)
    
len_rr, len_cc = 3, 3
time = 0
def opR():
    max_rr, max_cc = 0,0
    for idx,i in enumerate(A):
        tmp_A = defaultdict(int)
        for j in i:
            if j > 0:
                tmp_A[j] +=1
        tmp_A = sorted(tmp_A.items(), key= lambda x:(x[1],x[0]))
        A[idx] = []
        for tt in tmp_A:
            A[idx].append(tt[0])
            A[idx].append(tt[1])
        max_rr = max(max_rr, len(A))
        max_cc = max(max_cc, len(A[idx]))
    for i in range(max_rr):
        if len(A[i]) < max_cc:
            for j in range(max_cc - len(A[i])):
                A[i].append(0)
    return max_rr,max_cc
        
def opC(max_rr,max_cc,A):
    ret_max_r = 0
    tmp = [[0]*101 for _ in range(101)]
    for c in range(max_cc):
        tmp_A = defaultdict(int)
        for r in range(max_rr):
            if A[r][c] >0:
                tmp_A[A[r][c]] +=1
        tmp_A = sorted(tmp_A.items(), key= lambda x:(x[1],x[0]))
        ttt = 0
        cnt = len(tmp_A) *2
        while tmp_A:
            tmp[ttt][c] = tmp_A[0][0]
            tmp[ttt+1][c] = tmp_A[0][1]
            ttt+=2
            tmp_A.pop(0)
        ret_max_r = max(ret_max_r, cnt)
    A.clear()
    A = [[0]*max_cc for _ in range(ret_max_r)]
    for i in range(ret_max_r):
        for j in range(max_cc):
            A[i][j] = tmp[i][j]
    if ret_max_r < len(A):
        for _ in range(len(A) - ret_max_r):
            A.pop()
    return ret_max_r , max_cc, A

if  len_rr >= R and len_cc >= C and A[R-1][C-1] == k:
    print(0)
else:
    while time  <= 100:
        time +=1
        if len_rr>=len_cc:
            len_rr, len_cc = opR()
        else:
            len_rr, len_cc,A = opC(len_rr,len_cc,A)
        #100을 넘거면 자른다.
        if len_rr > 100 or len_cc > 100:
            if len_rr > 100:
                for _ in range(len_rr - 100):
                    A.pop()
            if len_cc > 100:
                for idx,a in enumerate(A):
                    A[idx] = a[:100]
        if  len_rr >= R and len_cc >= C:
            
            if  A[R-1][C-1] == k:
                break
    if time > 100:
        print(-1)
    else:
        print(time)