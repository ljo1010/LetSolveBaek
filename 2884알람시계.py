hour, mint =map(int, input().split())

if mint < 45:
    if hour ==0:
        hour = 23
        mint += 60
    else:
        hour -= 1
        mint += 60
print(hour, mint-45)
