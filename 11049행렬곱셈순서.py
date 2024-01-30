'''
행렬들의 곱을 했을 떄 얼만큼 곱했을 지를 구하는 문제이다.
그러므로 행렬들의 성질을 이해할 필요가 있어보인다.
행렬 2개가 있다고 가정해보자. 
2*3행렬과 3*6행렬이 있을 때 이 행렬이 가져야할 연산 횟수는 
2*3*6 = 36번의 연산횟수를 가진다.
위와 같은 연산횟수를 구하는 코드를 짜려면 D[1][n-1] + D[n][n] + a의 횟수를 가져야한다.

for문을 만들 때는 1개일때는 당연히 리턴 2개일 떄 앞 행렬의 행*뒤 행렬의 행*뒤 행렬의 열
3가지를 곱해서 리턴하도록 하자. 
행렬이 3개 이상일 때의 조건식도 있다.
D[s][i] + D[i+1][e] + a(s행렬의 행*i+1행렬의 행*e행렬의 열)
'''
import sys
input = sys.stdin.readline

n = int(input())
m = []
#d가 -1부터 시작하는 이유는 초기화를 해야하기 떄문에 그런거
d = [[-1 for j in range(n+1)] for i in range(n+1)]

m.append((0,0))

for i in range(n):
    x, y = map(int, input().split())
    m.append((x, y))

def execute(s, e):
    result = sys.maxsize
    if d[s][e] != -1:
        return d[s][e]
    if s == e:
        return 0
    if s + 1 == e:
        return m[s][0] * m[s][1] * m[e][1] #이거 할 때 행렬의 행 2개와 열 1개가 필요
    for i in range(s, e):
        result = min(result, m[s][0]*m[i][1]*m[e][1]+execute(s, i)+execute(i+1, e))
    d[s][e] = result
    return d[s][e]

print(execute(1, n))