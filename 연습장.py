import sys
input = sys.stdin.readline
N = int(input())
list = list(map(int, ' '.join(input().split())))
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = set() #이제 무조건 set으로 쓰자
count = 0

def DFS(start, visit):
    global count
    visit.add(start)

    for i in graph[start]:
        if i not in visit:
            visit.add(i)
            if list[i-1] == 1:
                count += 1
                continue
            DFS(i, visit)

for i in range(1, N+1):
    if list[i-1] == 0:
        continue
    visited = set()
    DFS(i, visited)
print(count)