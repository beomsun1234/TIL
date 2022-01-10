## 2차원 배열 회전

"""
# 90도
회전 전의 열 번호와 회전 후의 행 번호가 일치한다.
그리고 회전 후의 열은 N-1 에서 회전 전의 행을 뺀 값과 같다.
"""
def rotate_90(row,col,grid):
    ret = [[0]*col for _ in range(row)]

    #  원 배열의 값을 반환할 배열의 새로운 위치에 복사
    for r in range(row):
        for c in range(col):
            # 회전 전의 열과 후의 행이 일치
            ret[c][row-1-r] = grid[r][c]
    return ret

"""
180도

ex) 1 2 3         9 8 7
    4 5 6   ->    6 5 4
    7 8 9         3 2 1

상반되게 바뀐 것을 볼 수 있다.

회전 후의 행 번호는 N-1 의 값에서 전의 행 번호를 뺀 것과 같다.
회전 후의 열 번호는 N-1 의 값에서 전의 열 번호를 뺀 것과 같다.
"""
def rotate_180(row,col,grid):
    ret = [[0]*col for _ in range(row)]
    for r in range(row):
        for c in range(col):
            ret[row-1-r][col-1-c] = grid[r][c]

    return ret

"""
270도(반시계)

회전 후의 열과 전의 행이 일치한다.
후의 행 번호는 N-1 에서 전의 열 번호를 뺀 값과 일치한다.

"""

def rotate_270(row,col,grid):
    ret = [[0]*col for _ in range(row)]

    for r in range(row):
        for c in range(col):
            ret[col-1-c][r] = grid[r][c]

    return ret


"""
result[c][n-r-1] = arr[r][c]; // 시계 방향
result[n-c-1][r] = arr[r][c]; // 반시계 방향
result[n-r-1][c] = arr[r][c]; // 상하반전
result[r][n-c-1] = arr[r][c]; // 좌우반전

"""
test = [[1,2,3], [4,5,6], [7,8,9]]
print(rotate_90(len(test),len(test[0]),test))
print(rotate_180(len(test),len(test[0]),test))
