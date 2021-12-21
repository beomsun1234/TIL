    
"""
level 2 - 문자열 압축(2020 카카오블라인드)
문자열 계속 공부해야겠다... 먼가 쉬우면서도 어렵다.. 
문자열 패턴을 만들어서(자르기) 해야겠다고 생각했다. 우선 문자열을 잘라서 패턴을 만들고 난 후의 로직을 생각하지 못했었다..

풀이는 이렇다 자른 문자열을 패턴에 저장해, 반복문으로 이후의 문자열을 확인하여 해당 패턴이 있으면 카운트를 증가하고 없으면 ret문자열을 구성count+현재 패턴) 후 패턴을 우리가 현재 찾은 문자열로 바꾸어준다.
첫번째 패턴에 대한 반복이 종료되면 해당 패턴으로 했을 경우 문자열의 길이를 minVal과 비교하면서 교체해주고 ret문자열을 초기화해준다.
"""
def solution(s):
    answer = 0
    ret = ""
    minLen = 1001
    if len(s) == 1:
        return 1
    for i in range(1,len(s)//2+1):
        cnt = 1
        pattern = s[:i]
        for j in range(i,len(s),i):
            print(j)
            if s[j:j+i] == pattern:
                cnt+=1
            else:
                if cnt == 1:
                    cnt = ""
                ret += str(cnt) + pattern
                pattern = s[j:j+i]
                cnt = 1 
        if cnt == 1:
            cnt = ""
        ret+=str(cnt)+pattern
        minLen = min(minLen,len(ret))
        ret = ""
        print('--')
    return minLen
    