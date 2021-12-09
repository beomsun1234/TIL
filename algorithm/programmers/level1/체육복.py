"""
그리디 level 1 체육복


학생들의 번호는 체격 순으로 매겨져 있어,
바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다
ex)  4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다
체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야

처음 제출했을 때 4개를 통과하지 못했다.. 내가 생각한 방식은 주어진 lost와 reserve배열은 항상 정렬되어 주어진다고 생각했다. 질문을 살펴보니 정렬되지 않은 값도 들어갈 수 있었다.. 문제에 잘 좀 써주었으면 좋겠다..(항상 정렬된 배열을 준다는? 말과 같이 ㅠㅠ)  주어진 배열을 정렬하니 테스트케이스 1개를 통과하지 못했다.. 팁을 확인하니 여벌의 가져왔지만 잃어버렸으면 lost배열과 reserve배열에 값을 지워주는 식으로 해야한다는 팁을 받았다.. 나는 분명 해당 상황을 체크해줬다고 생각했지만 아니였던거다... 이전 로직은 만약 reserve의 값이  lost에 있지않았을때 다음로직으로 가도록했다만 정답이 아니었다... 여러 삽질 끝에 그냥 lost배열과 reserve배열에 값을 지워주는 식으로 진행하니 성공했다.


"""
def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    ## 체육복을 가져온 학생들을 set으로 저장.
    hasColthes = set([])
    for i in range(1,n+1):
        if not i in lost:
            hasColthes.add(i)
        if i in reserve:
            hasColthes.add(i)
        if i in lost and i in reserve: # 여벌의 가져왔지만 잃어버렸으면
            lost.remove(i)
            reserve.remove(i)
            
    print(hasColthes)
    # 여분의 체육복을 가져온 학생 중 일어버린 학생에게 빌려주는로직
    for hasNum in reserve:
        if hasNum -1 in lost:
            hasColthes.add(hasNum -1)
            lost.remove(hasNum -1)
        elif hasNum +1 in lost:
            hasColthes.add(hasNum +1)
            lost.remove(hasNum +1)
    return len(hasColthes)
