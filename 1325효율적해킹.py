import sys
import deque
input = sys.stdin.readline

n, m =map(int, input().split())

A = [[] for _ in range(n+1)]

ans = [0] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)

def BFS(v):
    queue = deque()
    visited = True

    while queue:
