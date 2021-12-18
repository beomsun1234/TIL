"""
2018 KAKAO BLIND RECRUITMENT 다트게임 level 1
간단했지만 40분 정도 걸린것같다.. 조건이 조금 까따롭다..
## 수정전 로직
flag =0 # 최대 두개까지만 바꿀수 있으므로 현재, 이전
for i in range(len(ret)-1,-1,-1):
    if flag == 2:
        break
    flag+=1
    ret[i] = ret[i]*2
## 수정 후 로직
if len(ret) > 1:
    ret[-1] = ret[-1] * 2
    ret[-2] = ret[-2] * 2
else:
    ret[-1] = ret[-1] * 2
    
"""
def solution(dartResult):
    ret = []
    for idx, point in enumerate(dartResult):
        if not point.isalnum(): # *,# 
            if point == '*':
               # *일 경우 최대 두개까지만 바꿀수 있으므로 현재, 이전
                if len(ret) > 1:
                    ret[-1] = ret[-1] * 2
                    ret[-2] = ret[-2] * 2
                else:
                    ret[-1] = ret[-1] * 2
            else: # #일 경우 자기자시만 음수
                ret[-1] = -ret[-1]
        else:
            if point in ('S','D','T'):
                if point == 'S': # 보너스 뒤에 문자는 숫자가 된다
                    if int(dartResult[idx-1]) == 0: # 뒤 문자가 0 이면 10이거나 or 0이다
                        if dartResult[idx-2] == '1': #그 뒤 문자가 1이면 10
                            ret.append(10)
                        else:
                            ret.append(0)
                    else:
                        ret.append(int(dartResult[idx-1]))
                elif point == 'D':
                    if int(dartResult[idx-1]) == 0:
                        if dartResult[idx-2] == '1':
                            ret.append(pow(10,2))
                        else:
                            ret.append(0)
                    else:
                        convertPoint = pow(int(dartResult[idx-1]),2)
                        ret.append(convertPoint)
                else:
                    if int(dartResult[idx-1]) == 0:
                        if dartResult[idx-2] == '1':
                            ret.append(pow(10,3))
                        else:
                            ret.append(0)
                    else:
                        convertPoint = pow(int(dartResult[idx-1]),3)
                        ret.append(convertPoint)
                    
    answer = 0
    return sum(ret)
    