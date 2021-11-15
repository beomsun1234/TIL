"""
프로그래머스 - 모의고사

input = int형 1차원 배열
ouput = int형 1차원 배열(주어진 input값과 정해진 3개의 패턴에서 가장 많이 맞은 사람의 번호 리턴)

constraint
- len(answer) <= 10,000 
- 정답은 1,2,3,4,5 중 하나
- 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬
 
1. 수포자 3명의 패턴을 배열에 저장한다.
2. 주어진 answers와 비교한다. 1번 패턴의 경우 5번을 돌면 다시 원래 숫자로 돌아오고, 2번의 경우 8번이 넘어가면 다시 원래 숫자로 돌아오고, 3번의 경우 10번이 넘어가면 다시 원래 숫자로 돌아온다. 
3. 위 패턴을 따라가면 1,2,3 번의 길이가 다르고 특정 숫자 이후에 원래 상태로 돌아와야하기에 주어진 answers 배열의 인덱스와 1,2,3 번 패턴의 길이를 나눈 나머지를(idx%len(answers))패턴 배열에 넣어준다.
ex) len(answers) = 6  1번패턴의 경우 -> 0%5 =0번째, 1%5 = 1번째 .... 6%6 = 0 
4. answers배열의 인덱스의 값과 특정 패턴 배열의 인덱스의(i%len(answers)) 값이 같으면 특정 socre 배열에 값을 증가시켜준다.
5. socre배열의 max와 socre의 특정 인덱스의 값과 비교해서 값이 같으면 ret배열에 넣어준다.

time - o(n) n개의 문제를 확인하기 때문에
space - o(1) 3명의 사람만을 이용하기에 


"""

def solution(answers):
    answer = []
    # 1번 1,2,3,4,5
    # 2번 2 - > 1,3,4,5
    # 3번 33 -> 11,22,44,55
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    for idx,an in enumerate(answers):
        if an == first[idx%len(first)]:
            score[0] += 1
        if an == second[idx%len(second)]:
            score[1] += 1
        if an == third[idx%len(third)]:
            score[2] +=1
    ret = []
    for idx, number in enumerate(score):
        if number == max(score):
            ret.append(idx+1)
    
    return ret