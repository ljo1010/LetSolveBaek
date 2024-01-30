from collections import deque

#방향 테스트 여기서 위 아래도 추가 해야함
dx =[0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
#n은 가로 m은 세로 h는 높이
m, n, h = map(int, input().split())

# A = [[[0]*m for _ in range(n)]for _ in range(h)]
# visited =[[False] *m for _ in range(n)]
visited_1 =[[[False]*m for _ in range(n)]for _ in range(h)]
# print(visited_1)
A = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

queue = deque()
# print(A)
for z in range(h):
    for y in range(n):
        for x in range(m):
            if A[z][y][x] == 1:
                queue.append((x, y, z))
                # visited_1[z][y][x] = True                
# print(A)
while queue:
    now = queue.popleft()
    for i in range(6):
        x = now[0] + dx[i]
        y = now[1] + dy[i]
        z = now[2] + dz[i]
        if  0 <= x < m and 0 <= y < n and 0 <= z < h and visited_1[z][y][x] == False and A[z][y][x] == 0:
            visited_1[z][y][x] = True
            A[z][y][x] = A[now[2]][now[1]][now[0]] + 1
            queue.append((x, y, z))
# print(A)
min_time = 0
flag = True

for z in range(h):
    for y in range(n):
        for x in range(m):
            # print(A[z][y][x])
            if A[z][y][x] == 0:
                flag = False
                # print(A[z][y][x])
                break
            else:
                min_time = max(A[z][y][x], min_time)
if flag:
    print(min_time-1)
else:
    print('-1')