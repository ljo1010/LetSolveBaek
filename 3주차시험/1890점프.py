'''
nxn의 판이 있고 가장 왼쪽 위부터 가장 오른쪽 아래까지
칸에 맞게 점프를 한다. 칸에 적힌 숫자는 현재 갈 수 있는 거리
오른쪽을 가거나 아래칸을 가야만한다. 0은 끝나는 지점이고 
항상 칸에 적힌 숫자만큼 오른쪽으로 가거나 아래칸으로 가야한다.
'''
import sys
input = sys.stdin.readline
n = int(input())

d = [[0]*n for _ in range(n)]
d[0][0] = 1

for i in range(n):
    d[i][i] = map(int, input().split())

for i in range(n):
    for j in range(n):
        

print(d[i][j])