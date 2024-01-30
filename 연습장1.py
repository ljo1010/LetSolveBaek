import sys
from collections import deque

input = sys.stdin.readline

dx =[0, 1, 0, -1]
dy = [1, 0, -1, 0]


r, c = map(int, input().split())
A = [[0]*c for _ in range(r)]
visited = [[False]*c for _ in range(r)]

for i in range(r):
    n = list


visited = [[False]*m for _ in range(N)] 

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    while  queue:
        now = queue.popleft()