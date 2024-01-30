import sys
from collections import deque

input = sys.stdin.readline


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

ans = []

def BFS(start, end):
    queue = deque()
    queue.append([start, 0])
    visited[start] = True
    flag = False

    while queue:
        node, dist = queue.popleft()

        if dist == k:
            ans.append(node)
            flag = True

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append([next_node, dist + 1])

    if not flag:
        print(-1)

BFS(x, k)
ans.sort()
if ans :
    for i in ans:
        print(i)