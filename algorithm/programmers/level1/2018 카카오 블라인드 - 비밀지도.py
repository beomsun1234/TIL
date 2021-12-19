"""
2018 KAKAO BLIND RECRUITMENT
[1차] 비밀지도 level1

"""
def convertBinary(num,n):
    binaryNumber = []
    while num >0:
        binaryNumber.append(num % 2)
        num = num//2
    if len(binaryNumber)!= n:
        for i in range(0,n-len(binaryNumber)):
            binaryNumber.append(0)
    binaryNumber.reverse()
    return binaryNumber
def solution(n, arr1, arr2):
    answer = []
    binaryArr1 = []
    binaryArr2 = []
    ret = []
    for i in range(len(arr1)):
        binaryArr1.append(convertBinary(arr1[i],n))
        binaryArr2.append(convertBinary(arr2[i],n))
        for j in range(n):
            if binaryArr1[i][j] == 1 or binaryArr2[i][j] == 1:
                ret.append("#")
            else:
                ret.append(" ")
        print("".join(ret))
        answer.append("".join(ret))
        ret = []
    return answer