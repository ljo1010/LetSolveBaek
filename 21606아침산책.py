# import sys
# sys.setrecursionlimit(10**6)

# input = sys.stdin.readline
# n = int(input()) #노드 개수
# tree =[[] for _ in range(n+1)] #트리구조
# visited = [False] *(n+1) #방문했는지 확인하기
# ans = 0
# inside = '0' + input() #안인지 바깥인지

# for _ in range(n-1):
#     a, b  = map(int, input().split())
#     tree[a].append(b)
#     tree[b].append(a)
    
#     if inside[a] == "1" and inside[b] == "1":
#         ans += 2

# def DFS(start):
#     visited[start] = True
#     inside_count = 0
   
#     for i in range(len(tree[start])):
#         if inside[tree[start][i]] == '1':
#             inside_count += 1
#         elif inside[tree[start][i]] and not visited[tree[start][i]]:
#             inside_count += DFS(tree[start][i])

#     return inside_count

# for j in range(1, n+1):
#     if inside[j] == '0' and not visited[j]:
#         result = DFS(j)
#         ans += result*(result-1)

# print(ans)

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