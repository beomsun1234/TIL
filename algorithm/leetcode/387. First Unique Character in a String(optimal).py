from collections import Counter as c

inputWord = input()
ret = -1
separatedWord = c(inputWord)

##print(separatedWord)

for idx,keyWord in enumerate(separatedWord):
    if(separatedWord.get(keyWord)==1):
        ret = idx
        ##print(ret)
        break

print(ret)

## 시간 복잡도 o(n)
## 공간 복잡도 o(1) -> 알파벳
## Constraints:
# 1 <= s.length <= 10^5
# s consists of only lowercase English letters.