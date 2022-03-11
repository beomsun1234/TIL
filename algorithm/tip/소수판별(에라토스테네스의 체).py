"""
소수판별(에라토스테네스의 체)
"""
def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
