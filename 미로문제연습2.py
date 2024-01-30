# # from collections import deque

# # dx = [0, 1, 0, -1]
# # dy = [1, 0, -1, 0]
# # N, M = map(int, input().split())

# # A = [[]*M for _ in range(N)]
# # visited =[[False] *M for _ in range(N)]

# # for i in range(N):
# #     numbers = list(input())
# #     for j in range(M):
# #         A[i][j] = int(numbers[j])

# # def BFS(i, j):
# #     queue = deque()
# #     queue.append((i, j))
# #     visited[i][j] = True

# #     while queue:
# #         now = queue.popleft()
# #         for i in range(4):
# #             x = now[0] + dx[k]
# #             y = now[1] + dy[k]
# #             if x >= 0 and x < N and y < M:
# #                 if A[x][y] !=0 and not visited[x][y]:
# #                     visited[x][y] =True
# #                     A[x][y] = A[now[0]][now[1]] + 1
# #                     queue.append((x, y))

# # BFS(0, 0)
# # print(A[N-1][M-1])
# from collections import deque

# #방향 테스트 여기서 위 아래도 추가 해야함
# dx =[0, 1, 0, -1, 1, -1]
# dy = [1, 0, -1, 0]
# #n은 가로 m은 세로 h는 높이
# n, m, h = map(int, input().split())

# A = [[]*m *h for _ in range(n)]
# visited =[[False] *m for _ in range(n)]

# for i in range(n):
#     num = list(input())
#     for j in range(m):
#         A[i][j][h] = int(num[j])


#     queue.append((i, j))
#     visited[i][j] = True

#     while queue:
#         now = queue.popleft()
#         for i in range(4):
#             x = now[0] + dx[k]
#             y = now[1] + dy[k]
#             if x >= 0 and x < N and y < M:
#                 if A[x][y] !=0 and not visited[x][y]:
#                     visited[x][y] =True
#                     A[x][y] = A[now[0]][now[1]] + 1
#                     queue.append((x, y))

# BFS(0, 0)
# print(A[N-1][M-1])


# def BFS(i, j):
#     queue = deque()
#     queue.append((i, j))
#     visited[i][j]
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n, m = map(int, input().split())

graph = [[0]*m for _ in range(n)]
visited = [[False] *m for _ in range(n)]

for i in range(n):
    n = list(input())
    for j in range(m):
        graph[i][j] = int(n[j])

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x >= 0 and y >= 0 and x < n and y < m:
                if graph[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    graph[x][y] = graph[now[0]][now[1]] + 1
                    queue.append((x, y))
BFS(0, 0)
print(graph[n-1][m-1])
