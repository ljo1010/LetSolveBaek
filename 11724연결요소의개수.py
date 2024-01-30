# import sys
# sys.setrecursionlimit(10000)
# input = sys.stdin.readline

# n = int(input())
# m = int(input())

# A = [[]for _ in range(n+1)]

# for _ in range(m):
#     s, e = map(int,input().split())
#     A[s].append(e)
#     A[e].append(s)

# visited = [False] * (n+1)
# count -= 1

# def DFS(v):
#     visited[v] = True
#     global count
#     count += 1
#     for i in A[v]:
#         if not visited[i]:
#             DFS(i)

# DFS(1)
# print(count)

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]	

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)				# 양방향
visited = [False] * (N+1)
count = -1

def DFS(v):
    visited[v] = True
    global count
    count += 1
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

DFS(1)
print(count)