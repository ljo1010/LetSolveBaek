# import sys
# input = sys.stdin.readline
# n = int(input())
# space = []

# for i in range(n):
#     a, b = map(int, input().split())
#     space.append([a, b])

# space.sort(key=lambda x: x[0])
# space.sort(key=lambda x: x[1])

# count = 1
# end = space[0][1]
# for i in range(1, n):
#     if space[i][0] >= end:
#         count += 1
#         end = space[i][1]

# print(count)
import sys
input = sys.stdin.readline

n = int(input())
space = []

for i in range(n):
    a, b = map(int, input().split())
    space.append([a, b])

space.sort(key=lambda x: x[0])
space.sort(key=lambda x: x[1])

count = 1
end = space[0][1]
for i in range(1, n):
    if space[i][0] >= end:
        count += 1
        end = space[i][1]

print(count)