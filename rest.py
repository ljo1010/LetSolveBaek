def hanoi(n, a, b, c):
    if n == 1:
        print(n)
    else:
        hanoi(n-1, a, c, b)
        print(n)
        
        hanoi(n-1, b, a, c)
        print(f"{a} {b}")

n = int(input(" "))
hanoi(n, 'A', 'B', 'C')        