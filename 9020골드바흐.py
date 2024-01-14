import math

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False # 소수 아님
    return True

a1 = int(input())

for _ in range(a1):
    n = int(input())
    a, b = n//2, n//2

    for _ in range(n//2):
        if is_prime_number(a) and is_prime_number(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1