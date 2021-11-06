##  find the first non-repeating character in it and return its index. If it does not
inputWord = input()
checkChar = []
ret = -1
countChar = []
for idx,c in enumerate(inputWord):  
    if(c not in checkChar):
        checkChar.append(c)
        countChar.append(int(0))
        for j in range(0,len(inputWord)):
            if(checkChar[idx] == inputWord[j]):
                countChar[idx]+=1
    else:
        checkChar.append(0)
        countChar.append(-1)       

for idx,count in enumerate(countChar):
    if(count==1):
        ret = idx
        break       

print(ret)

## 시간 복잡도 o(n^2)