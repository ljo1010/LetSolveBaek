import sys
import itertools
n, s = map(int, sys.stdin.readline().split())

a = [int(input()) for _ in range(n)]

for i in itertools.combinations(a, s):
    if sum(i) == s:
        for j in sorted(i):
            print(j)
        break