# Roman to Integer

"""""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

ds - 딕셔너리(맵 구조)

d = {'I':1, 'V':5, 'X':10}

입력 받은 문자열을 확인하여 조건에 부합시키는지 확인하고 값을 매겨주고 값을 배열에 넣어준 후 계산한다.
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer.
    ex) IV = 4, IX = 9
    ex) IV = [-1, 5]로 바꾼 후 배열의 값을 계산하면 4가된다. 즉 현재 값이랑 다음값이랑 비교해서 현재 값이 작으면 현재 값을 음수로 바꿔준다.
"""""
symbolChr = {
    'I':1, 'V':5 , 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
}

str = input()
ret = []

for idx,chr in enumerate(str):
    ret.append(symbolChr.get(chr))

for idx,r in enumerate(ret):
    nextIdx = idx+1
    if(nextIdx< len(ret)):
        if r < ret[nextIdx]:
            ret[idx] *= -1

print(sum(ret))


# 제출코드

class Solution: 
    def romanToInt(self, s: str) -> int: 

        ret = []
        symbolChr = {
            'I':1, 'V':5 , 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 
        }

        for idx,chr in enumerate(s):
            ret.append(symbolChr.get(chr))

        for idx,r in enumerate(ret):
            nextIdx = idx+1
            if(nextIdx< len(ret)):
                if r < ret[nextIdx]:
                    ret[idx] *= -1

        return (sum(ret))