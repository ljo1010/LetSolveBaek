import sys
from queue import deque

n, m, v = map(int, input().split())
node = [[] for _ in range(n+1)]
visited = [False] * (n+1)
dfs = []
bfs = []

for i in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for j in range(n+1):
    node[j].sort()

def DFS(v):
    visited[v] = True
    dfs.append(v):
    for i in node[v]:
        if(visited[i] == 0):
            DFS(i)

def BFS(v):
    visited = True
    bfs.append(v)
    queue = dequeu([v])

    while queue:
        curr = queue.popleft()