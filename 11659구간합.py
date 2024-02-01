import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

d = [0] * (n+1)

for _ in range(n):
    d[_+1] = d[_]+num[_]

for _ in range(m):
    s, e = map(int, input().split())
    print(d[e] - d[s-1])