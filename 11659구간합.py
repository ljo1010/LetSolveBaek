# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# num = list(map(int, input().split()))

# prefix_sum = [0]
# temp = 0

# for i in num:
#     temp = temp + i
#     prefix_sum.append(temp)

# for i in range(n):
#     s, e = map(int, input().split())
#     print(prefix_sum[e] - prefix_sum[s-1])

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

prefix_sum =[0]
temp = 0

for i in range(n):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])