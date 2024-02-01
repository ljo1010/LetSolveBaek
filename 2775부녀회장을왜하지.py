import sys
input = sys.stdin.readline

t = int(input())


for i in range(t):
    floor = int(input())
    room = int(input())
    d = [[0]*(room+1) for i in range(floor+1)]

    for i in range(room+1):
        d[0][i] = i
    for i in range(floor +1):
        d[i][1] = 1
    for i in range(1, floor+1):
        for j in range(2, room+1):
            d[i][j] = d[i-1][j]+d[i][j-1]
    print(d[floor][room])