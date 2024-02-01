'''
d에다가 계산된 값을 저장한다.
%를 사용해서 나머지가 0이 되면 계산된 횟수 +1을 해주면 된다.
'''
# import sys
# input = sys.stdin.readline

# n = int(input())
# d = [0] * (n+1) #d에 계산된 값을 저장 n+1인 이유는 

# for i in range(2, n+1):
#     d[i] = d[i-1] +1
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i//3]+1)
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i//2]+1)
# print(d[n])
import sys
input = sys.stdin.readline

n = int(input())
d = [0]* (n+1)

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)

print(d[n])