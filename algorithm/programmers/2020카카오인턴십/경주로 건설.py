"""
프로그래머스 2020 카카오 인턴십 경주로 건설

https://programmers.co.kr/learn/courses/30/lessons/67259

"""
# 시작위치가 2개이므로 두번 돌려한다.
# 2-> - 3-> |
from collections import deque
def bfs(board, start_r, start_c, cost,head):
    # 0-> 위 1->왼, 2->아래,  3->오른
    dirs = [(-1,0), (0,-1), (1,0), (0,1)]
    
    len_r = len(board) 
    len_c = len(board) 
    #거리표시
    visited = [[float("inf")] * len_c for _ in range(len_r)]
    visited[0][0] = 0
    
    q = deque()
    q.append((0, 0, 0, head))
    
    while q:
        now_r,now_c, cost, dir = q.popleft()
        # 0-> 위 1->왼, 2->아래,  3->오른
        for i in range(4):
            next_r = now_r + dirs[i][0]
            next_c = now_c + dirs[i][1]
            #직진로 가격
            next_cost = cost +100
            if dir != i:
                #방향이 다르면 코너컨설(500원)
                next_cost +=500
            if 0<=next_r<len_r and 0<=next_c<len_c:
                #벽이 아니면
                if board[next_r][next_c] == 0: 
                    # 다음 건설지역의 건설비용이 더 저렴하면 변경
                    if visited[next_r][next_c] > next_cost:
                        visited[next_r][next_c] = next_cost
                        q.append((next_r,next_c,next_cost, i))
    ## 최종 건설 목적지 배열의 끝      
    return visited[-1][-1]
def solution(board):
    answer = 0
    ## 아래쪽, 오른쪽
    answer = min(bfs(board,0,0,0,2), bfs(board,0,0,0,3))
    return answer