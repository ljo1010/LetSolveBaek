# def move(no: int, x: int, y:int) -> None:

#     if no > 1:
#         move(no-1, x, 6-x-y)
    
#     print(f'{x}{y}')
#     if no > 1:
#         move(no-1, 6-x-y, y)

# n =int(input())
# print(2**n-1)
# if n <= 20:
#     print(move(n, 1, 3))

def move(num, start, dest):
    if num > 1:
        move(num -1 , start, 6-start-dest)
    print(start, dest)

    if num > 1:
        move(num-1, 6-start-dest, dest)
    print(move(num, 1, 3))