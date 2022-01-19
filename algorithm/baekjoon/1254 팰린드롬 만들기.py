"""
팰린드롬 만들기 - 1254

너무 쉽게 생각했었다.. 마지막 문자열을 제외하고 마지막 전 부터 0까지 -1 해가면서 문자열을 붙이고 팰린드롬을 
체크하는 방식으로 접근했었다.. 예제 4번 케이스인 abdfhdyrbdbsdfghjkllkjhgfds에서 닶이 달랐다..

변경한 로직은 이렇다. 입력한 문자열의 i번째(0부터시작) 인덱스부터 시작하는 문자여을 자른 후 (s[idx:]) 해당 문자열의 팰린드롬 여부를 찾아서
팰린드롬일 경우 해당 문자열의 시작인덱스 + 주어진 문자열의 길이를 프린트하면 정답이다.

ex) abab -> 
 idx subS
  0   abab   -> isPalindrome(subS) ? x 
  1   bab     -> isPalindrome(subS) ? O

  abab가 최소 팰린드롬이 되려면
a bab a
  ^ 
idx = 1이며 최소팰린드롬 = idx+len(S)

즉 인덱스가 0인 지점부터 차례대로 조사하며 팰린드롬이 되는 최소한의 시작 위치를 찾는 것이다.

어차피 중간에 팰린드롬이 생기는 것은 아무 의미가 없기 때문에특정 인덱스부터 문자열의 맨 마지막까지 팰린드롬이 되는 부분 문자열을 찾으면,
 (특정인덱스+원래 문자열의 크기)가 최소 팰린드롬의 길이가 되는 것이다.



"""

def isPalindrome(s):
    p = s[::-1]
    if s == p:
        return True
    
    return False

S = input()

if isPalindrome(S):
    print(len(S))
else:
    for i in range(len(S)):
        tmp = S[i:]
        if isPalindrome(tmp):
            print(tmp)
            answer = len(S) + i
            break
    
    print(answer)
