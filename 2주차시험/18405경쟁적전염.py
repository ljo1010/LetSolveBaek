import sys
input = sys.stdin.readline
n = int(input())
#방향성 추가
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

graph = [[]*n for _ in range(n)]
visited = [[False]*m for _ in range(n)]

for _ in range(n):


def BFS(v):
