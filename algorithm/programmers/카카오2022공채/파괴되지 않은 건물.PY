"""
프로그래머스 -  파괴되지 않은 건물(2022 KAKAO BLIND RECRUITMENT)

for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            for i in range(r1,r2+1):
                for j in range(c1,c2+1):
                    board[i][j] -= degree
        if type == 2:
            for i in range(r1,r2+1):
                for j in range(c1,c2+1):
                    board[i][j] += degree
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer+=1


"""
def solution(board, skill):
    answer = 0
    # skill
    # [type, r1, c1, r2, c2, degree]
    # type이 1이면 degree만큼 건물의 내구도를 낮춥니다.
    # type이 2이면 degree만큼 건물의 내구도를 높입니다.
    tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        # 누적합 기록
        if type == 1:
            tmp[r1][c1] -= degree
            tmp[r2+1][c2+1] -= degree
            tmp[r1][c2+1] += degree
            tmp[r2+1][c1] += degree
        elif type == 2:
            tmp[r1][c1] += degree
            tmp[r2+1][c2+1] += degree
            tmp[r1][c2+1] -= degree
            tmp[r2+1][c1] -= degree
    #가로방향에 대해서 누적합 계산
    for rr in range(len(board)):
        for cc in range(len(board[0])):
            tmp[rr][cc+1] += tmp[rr][cc]
    #세로방향에 대해서 누적합 계산
    for cc in range(len(board[0])):
        for rr in range(len(board)):
            tmp[rr+1][cc] += tmp[rr][cc]
    #board와 대입하여 계산
    for rr in range(len(board)):
        for cc in range(len(board[0])):
            board[rr][cc]+=tmp[rr][cc]
            if board[rr][cc] >0:
                answer+=1
    return answer