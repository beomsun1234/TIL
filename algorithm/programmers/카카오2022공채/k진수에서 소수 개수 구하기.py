"""
프로그래머스 카카오 블라인드 2022 k진수에서 소수 개수 구하기 

간단했다.. 문제를 잘 읽어야했다.. 처음에 다른길로 빠질뻔했다. n을 k진수로 변환 후 조건에 맞는 수를 뽑는데 이 부분을 이상하게 이해해서 시간을 조금 낭비했다..
문제를 다시 읽어보니 P는 각 자릿수에 0을 포함하지 않는 소수입니다. 여기 부분에 큰 힌트를 얻고 바로 제출하니 통과 했다.. 문제좀 자세히 읽어야겠다..

"""

# 소수 판별
def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
#k진수로 변환
def convert_k(n,base):
    tmp = ''
    while n > 0:
        n, mod = divmod(n, base)
        tmp += str(mod)
    
    return tmp[::-1]

def solution(n, k):
    answer = 0
    #진법변환
    num = convert_k(n,k)
    # 0을 포함하지 않는다.
    prime_arr = num.split("0")
    for number in prime_arr:
        if nn == '':
            continue
        li_number = int(number)
        if is_prime(li_number):
            answer+=1
    return answer