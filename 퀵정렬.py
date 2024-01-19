import math

a = int(input())
num = map(int, input().split())
prime_num = 0

def is_prime_number(x):
    error = 0
    if x == 1:
        return None
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            error += 1
            return error
        else:
            prime_num += 1
print(is_prime_number(prime_num))

