

number = 0
x = []

while True:
    s = input(f'x[{number}]값을 입력하세요: ')
    if s == 'End':
        break
    x.append(int(s))
    number += 1

print(number)
print(max(x))