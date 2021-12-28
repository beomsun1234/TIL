"""
접근방식은 간단했다.  #을 어떻게 처리해줄지 고민했는데 C# ->  c와 같이 사용하지 않는 문자로 치환해주었다.
하지만 정확성 90으로 통과하지 못했다.. 내 접근 방법은 아래와 같다

1. musicinfos를 반복문으로 확인한다. 현재 확인 하려는 musicinfo를 문자열 ','를 기준으로 잘라준다.
   잘라준 문자열 인덱스가 0 = 재생시작시간, 1= 재생종료시간, 3=곡명, 4 = 멜로디로 나누어준다.
2. 재생시작시간과 종료시간은 hh:mm 이므로 ":"를 기준으로 hh, mm으로 나누어준다.
3. ((종료H - 시작H) * 60) + (종료M-시작M) 해당 계산식으로 플레이시간을 구해준다.
4. len(melody) < playTime 일 경우 멜로디를 이어준다.
5. else 멜로디를 잘라준다
6. 구해진 멜로디 배열을 만들고 입력받은 멜로디와 비교해서 있으면 해당 인덱스의 곡명을 반환한다.

이렇게 할 경우 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환해야하는데 이러지 못한다..

로직을 변경해주니 성공했다. 입력받은 멜로디와 비교해서 해당 멜로디가 있을 경우 곡명,playTime,index를 같이 넣어주고 만약 여러개일 경우 후보들을 playTime이 크고, index가 작은 순으로 정렬해준다.
qq = sorted(qq,key = lambda x : (-x[1],x[2])) 이러면 성공이다.

def solution(m, musicinfos):
    answer = ''
    test = []
    ##  C, C#, D, D#, E, F, F#, G, G#, A, A#, B 
    tt = []
    for musicinfo in musicinfos:
        mInfo = musicinfo.split(',')
        startTime = mInfo[0].split(':')
        finshTime = mInfo[1].split(':')
        melody = mInfo[3].replace("F#", "f").replace("C#","c").replace("A#","a").replace("G#","g").replace("D#","d")
        hhS, mmS = startTime[0], startTime[1]
        hhF, mmF = finshTime[0], finshTime[1]
        ## 플레이시간
        playTime = ((int(hhF)-int(hhS))*60)+(int(mmF) - int(mmS))
        # 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다.
        if len(melody) < playTime:
            repet = abs(playTime - len(melody))
            for i in range(repet):
                melody+=melody[i]
        # 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생
        else:
            melody = melody[:playTime]
        test.append(melody)
    print(test)
    m = m.replace("F#", "f").replace("C#","c").replace("A#","a").replace("G#","g").replace("D#","d")
    # 멜로디 비교하기
    for idx, musicinfo in enumerate(test):
        if m in musicinfo:
            ret = musicinfos[idx].split(",")
            return ret[2]

    return '(None)'

"""
def solution(m, musicinfos):
    answer = ''
    melodyList= []
    ##  C, C#, D, D#, E, F, F#, G, G#, A, A#, B 
    tt = []
    for musicinfo in musicinfos:
        mInfo = musicinfo.split(',')
        startTime = mInfo[0].split(':')
        finshTime = mInfo[1].split(':')
        melody = mInfo[3].replace("F#", "f").replace("C#","c").replace("A#","a").replace("G#","g").replace("D#","d")
        hhS, mmS = startTime[0], startTime[1]
        hhF, mmF = finshTime[0], finshTime[1]
        ## 플레이시간
        playTime = ((int(hhF)-int(hhS))*60)+(int(mmF) - int(mmS))
        # 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다.
        if len(melody) < playTime:
            repet = abs(playTime - len(melody))
            for i in range(repet):
                melody+=melody[i]
        # 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생
        else:
            melody = melody[:playTime]
        melodyList.append(melody)
    m = m.replace("F#", "f").replace("C#","c").replace("A#","a").replace("G#","g").replace("D#","d")
    # 멜로디 비교하기
    qq = []
    for idx, musicinfo in enumerate(melodyList):
        if m in musicinfo:
            ret = musicinfos[idx].split(",")
            startTime = ret[0].split(':')
            finshTime = ret[1].split(':')
            hhS, mmS = startTime[0], startTime[1]
            hhF, mmF = finshTime[0], finshTime[1]
            playTime = ((int(hhF)-int(hhS))*60)+(int(mmF) - int(mmS))
            ## 조건이 일치할 경우를 대비해서 index와 time도 함께 기록
            qq.append([ret[2],playTime,idx])
    if not qq:
        return '(None)'
    if len(qq) == 1:
        return qq[0][0]
    else:
        ## 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
        qq = sorted(qq,key = lambda x : (-x[1],x[2]))
        return qq[0][0]
    