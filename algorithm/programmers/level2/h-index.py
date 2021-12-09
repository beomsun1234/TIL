

"""
정렬 level2 h-index
문제를 이해하지 못했다.. H-index에 대해서 잘정리된 링크이다.
https://www.ibric.org/myboard/read.php?Board=news&id=270333
해당 링크에서 너무 잘 설명해주셔서 정말정말 쉽게 풀수있었다.
내림차순으로 정렬해서 현재 피인용횟수가 인덱스보다 작거나 같으면 해당 인덱스를 리턴해주면된다.

--처음 제출 코드 
def solution(citations):
    answer = 0
    citations=sorted(citations,reverse=True)
    print(citations)
    for i in range(len(citations)):
        if citations[i] <= i:
            return i
            
해당 로직으로만 접근했더니 다 파란색이 뜬것처럼보여 좋아했지만... 테스트케이스 9번을 통과하지 못했다... 이것때문에 계속 고민한 것 같다... 만약 저 조건에 포함되지 않으면 ex)[22, 42], 2 와 같이 익덱스보다 값이 월등히 큰 수로 나올경우 주어진 citations의 값을 리턴해주면된다.

위 방법을 몰라서 9번에서 고생했다 ㅠㅠ

어떤분의 아이디어를 보고 감탄했다..

주어진 citations 그래프로 나태내고 해당 그래프에서 가로세로가 h인 정사각형을 떠올리고 정사각형의 한 변의 길이가 가장 최대일때를 계산하는 방법이다. 와.... 감탄만 나온다...

def solution(citations):
    citations.sort(reverse=True)
    length = len(citations)
    answer = 0
    for i in range(length):
        if citations[i] < i+1:
            break
        else:
            answer = i+1
    return answer


"""

def solution(citations):
    answer = 0
    citations=sorted(citations,reverse=True)
    print(citations)
    for i in range(len(citations)):
        if citations[i] <= i:
            return i
    return len(citations)
    

