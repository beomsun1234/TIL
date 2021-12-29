"""
프로그래머스 - 2018 카카오 블라인드[3차] 파일명 정렬

정말 간단했다.. 정렬법 대로 파일명을 정렬하면 끝이다. 나는 tail을 신경쓰지 않았는데 다른 분들 풀이를 보면 tail도 잘라서 넣어준 것 같다. 나는 그냥 tail은 인덱스를 넣어 주었다.
header에는 숫자가 나오기전 문자의 첫번째를 넣어준다. ex) foo9.txt -> 내 정규식을 사용하면 이렇게 나온다 [foo, .text] 여기서 첫번째를 가져다 사용하면 된다.
number는 숫자들만 가져와서 그중 첫번재만 가져온다. ex) foo010bar020.zip 정규식 - [010, 020] 첫번째를 사용하고 int형으로 형변환시 10이 된다.
tail에는 해당 인덱스를 넣어준다.
만들어진 head, number, tail을 ret배열에 넣어주고

최정적인 ret배열을 head와 number를 기준으로 정렬한다. sort(key = lambda x: (x[0].lower(), x[1])) 만약 header가 같다면 number를 비교한다. ret배열의 인덱스를 가져와 files에 대입하여 answer에 추가해준다.
"""
import re
def solution(files):
    answer = []
    ret = []
    for idx,file in enumerate(files):
        header = re.findall('[^0-9]+', file)[0]
        number = int(re.findall("\d+", file)[0])
        tail = idx
        ret.append([header,number,tail])
    ret.sort(key = lambda x: (x[0].lower(), x[1]))
    for i in ret:
        answer.append(files[i[2]])
    return answer
    