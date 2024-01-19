# N, M = map(int, input().split())
# A, B = [], []

# for _ in range(N):
#     row = list(map(int, input().split()))
#     A.append(row)

# for _ in range(N):
#     row = list(map(int, input().split()))
#     B.append(row)

# for i in range(N):
#     for j in range(M):
#         print(A[i][j]+B[i][j], end=' ')
#     print()

n , m = map(int, input().split())
a, b = []

for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)

for _ in range(m):
    row = list(map(int, input().split()))
    b.append(row)

for i in range(n):
    for j in range(m):
        print(a[i][j]+b[i][j], end=' ')
    print()

