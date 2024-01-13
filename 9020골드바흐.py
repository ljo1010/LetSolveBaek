def is_prime_number(x):
    x=int(input())
    for i in range(2, x):
        if x % i == 0:
            return False # 소수 아님
    return True