# # # 이 문제에서 핵심은 a, b를 단순히 곱하기만 해서는 시간복잡도가 o(n)이기에 
# # # 분할정복이용 시간복잡도를 절반 수준으로 줄여야한다.o(logn)
# # # 이 문제는 분할 정복 처럼 a와 b를 나누어 
# # import sys
# # A, B, C = map(int, sys.stdin.readline().split())

# # def DC(a, b):
# #     if b == 1:
# #         return a % C
# #     temp = DC(a, b // 2)
# 분할정복을 함수로 만들어서 
# #     if b % 2 == 0:
# #         return temp * temp % C
    
# #     else:
# #         return temp * temp * a % C
# # print(DC(A, B))

import sys
A, B, C = map(int, sys.stdin.readline().split())

def DaC(a, b):
    if b == 1:
        return a%C
    temp = DaC(a, b//2)

    if b % 2 == 0:
        return temp * temp % C
    else:
        return (temp * temp * a) % C
print(DaC(A, B))