
"""
# 2020 카카오 겨울 인턴, 키패드 누르기
엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.

왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.

오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.

가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

Input  = 순서대로 누를 번호가 담긴 배열 numbers, 손잡이인지 오른손잡이인 지를 나타내는 문자열 hand
Output = 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 
Constraints
- numbers 배열의 크기는 1 이상 1,000 이하입니다.
- numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
- hand는 "left" 또는 "right" 입니다.
- "left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
- 왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.

DS - 완전탐색

time = O(N)
space = O(N)

처음에 2,5,8,0의 값을 어떤식으로 처리해줘야할지 감이 안잡혀서 하드코딩을 구현했다... 모든 경우를 조건 문으로 나열해 준 것이다.. 맞았는데 틀린것 같은 기분이었다.. 다른 사람의 풀이를 보니 좌표를 생각하고 풀었다.. 나도 처음에는 거리로 접근했지만 어떤식으로 비교해야할지 몰랐다.... 다른 사람의 풀이를 보니 밑에와 같은 변화를 가지게 된다.
     (-3)
       ▲
(-1) ◀   ▶ (+1)
       ▼
      (+3)
예를 들어 5에서 위로 한칸 이동하면 -3의 변화를 거쳐 2가 된다. 또, 8에서 아래로 한칸 이동하면 +3을 변화를 거쳐 키패드 0에 대응하는 11이 되는 것이다. 이에 따라 마지막 손의 위치와 2,5,8,0 원소간 절댓값을 구하고 이를 3으로 나눈 몫과 나머지를 더하면 키패드 상의 거리를 구할 수 있다. 이들을 비교하여 거리가 가까운 손을 구해 'L'과 'R'을 정하고 같을 경우에는 hand 값을 활용하면 문제를 해결할 수 있다.


좋아요를 가장 많이 받은 풀이법


def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer





"""

def solution(numbers, hand):
    answer = ''
    
    left = 10
    right = 12
        
    for number in numbers:
        print(left,right)
        if number in (1,4,7): 
            answer+="L"
            left = number
        elif number in (3,6,9):
            answer+="R"
            right = number
        else:
            if number == 0:
                number = 11 
            # 예를 들어 5에서 위로 한칸 이동하면 -3의 변화를 거쳐 2가 된다. 또, 8에서 아래로 한칸 이동하면 +3을 변화를 거쳐 키패드 0에 대응하는 11이 되는 것이다. 이에 따라 마지막 손의 위치와 2,5,8,0 원소간 절댓값을 구하고 이를 3으로 나눈 몫과 나머지를 더하면 키패드 상의 거리를 구할 수 있다. 이들을 비교하여 거리가 가까운 손을 구해 'L'과 'R'을 정하고 같을 경우에는 hand 값을 활용하면 문제를 해결할 수 있다.
            leftDist = abs(number - left)
            rightDist = abs(number - right)
            if leftDist // 3 + leftDist % 3 < rightDist // 3 + rightDist % 3 :
                left = number
                answer += 'L'
            elif leftDist // 3 + leftDist % 3 > rightDist // 3 + rightDist % 3 :
                right = number
                answer += 'R'
            elif leftDist // 3 + leftDist % 3 == rightDist // 3 + rightDist % 3 :
                if hand == 'left' :
                    left = number
                    answer += 'L'
                else :
                    right = number
                    answer += 'R'
    print(answer)
    return answer
