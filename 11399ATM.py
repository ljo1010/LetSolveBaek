# import sys
# input = sys.stdin.readline

# n = int(input())
# D = [[0 for j in range(2)]for i in range(n+1)]

# D[1][1] = 1
# D[1][0] = 0

# for i in range(2, n+1):
#     D[i][0] = D[i-1][0] + D[i-1][1]
#     D[i][1] = D[i-1][0]

# print(D[n][0] + D[n][1])
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0

for i in range(1, n+1):
    result += sum(arr[0:i])

print(result)