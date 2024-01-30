import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())

visited = [False] * (N+1)
tree = [[] for _ in range(N+1)]
ans = [0] * (N+1)

#트리에 데이터 저장
for _ in range(1, N):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

def DFS(num):
    visited[num] =True
    for i in tree[num]:
        if not visited[i]:
            ans[i] = num
            DFS(i)

DFS (1)

for i in range(2, N+1):
    print(ans[i])

def DFS(n):
    visited[n] = True
    for i in A[v]:
        if not visited:
            DFS(n)