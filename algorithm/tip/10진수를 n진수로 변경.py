#n진수로 변환
def convert_n(n,base):
    tmp = ''
    while n > 0:
        n, mod = divmod(n, base)
        tmp += str(mod)
    return tmp[::-1]
