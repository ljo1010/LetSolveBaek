hour, min =map(int, input().split())

if min == 60:
    hour += 1
    min = 0
