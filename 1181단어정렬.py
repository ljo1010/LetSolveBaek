#프로그래밍은 순차적이기 떄문에 순서가 매우 중요하다 순서가 틀리면 
#문제도 틀리게 된다.
n = int(input())
lis = [str(input()) for i in range(n)]

lis = list(set(lis))
lis.sort()
lis.sort(key = len)

for i in lis:
    print(lis)