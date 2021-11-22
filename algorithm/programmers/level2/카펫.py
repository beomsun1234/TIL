"""
프로그래머스 카펫 Level 2
Input  = brown -> int , yellow -> int
Output = 정수형 1차원  배열,
constraints
- 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
- 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
- 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

DS - 완전탐색

1. 노랑색의 세로를 1부터 시작하여 n+1 까지로 설정하고 탐색을 진행
2. 만약 노랑색의 세로와 노랑색의 격자 개수를 나눈 나머지가 0이 아니면 정사각형 또는 직사각형이 될 수 없다. ex) 주어진 테스트 케이스 3번 일 경우 yellow 격자의 수 24, 세로를 5로 설정하면 해당 케이스는 가로가 4.8로 사각형 또는 정사각형이 될 수 없다,
3. 설정한 세로와 노랑색의 격자 개수를 나눈 나머지가 0이면 탐색 진행
4. 가로를 설정해 준다. 가로는 세로*가로 = yellow 이니 현재 세로와 yellow가 주어줬으니 가로 = yellow/세로 한 값이다.
5. 브라운은 노랑을 둘러 싸고 있다. 우리가 구한 노랑색의 가로와 세로를 통해 현재 만든 노랑색 사각형을 둘러싼 브라운의 값을 구할 수 있다. 이렇게 구한 브라운의 값이 주어진 브라운의 값과 같으면 가로와 세로 +2 해준 값을 정답에 넣어준다.

time - o(n) yellow의 격자의 수 n 만큼 탐색하기 때문
space - o(1) 

"""

def solution(brown, yellow):
    answer = []
    tmp_brown = 0
    yellow_row = 0
    # 노랑의 세로 길이를 1부터 yellow수 만큼 탐색
    for yellow_col in range(1,yellow+1):
        
        ## 현재 가로의 길이는, yellow // yellow_col 
        yellow_row = yellow // yellow_col
        
        # yellow가 세로길이로 딱 나누어 떨어지지 않으면 직사각형, 정사각형 모양이 되지 않으므로 넘어감
        if yellow % yellow_col != 0:
            print(yellow_col)
            print(yellow % yellow_col)
            continue
            
        # 세로가 가로보다 크면 조건이 만족되지 않으므로 패스
        if yellow_row < yellow_col:
            continue
            
        # a = 가로, b = 세로
        # 브라운이 옐로우를 감싸고 있기에 
        # (a - 2 ) * (b - 2) = yellow
        # 2a + 2b = brown +4
        tmp_brown = (yellow_col*2)+(yellow_row*2) +4
        
        if tmp_brown == brown:
            answer.append(yellow_row+2)
            answer.append(yellow_col+2)
    return answer