import sys
from queue import PriorityQueue

input = sys.stdin.readline
#도시의 개수를 넣어줌
n = int(input())#노드수
m = int(input())#엣지수

visit = [False]*(n+1)
board  = [[] for _ in range(n+1)]
route = [sys.maxsize]* (n+1) #현재위치


for _ in range(m):
    start ,end, weight = map(int, input().split())
    board[start].append((end, weight))
    
start_index, end_index = map(int, input().split())

# print(route)

def dijkstra(start, end):
    pq = PriorityQueue()
    pq.put((0, start))

    route[start] = 0

    while pq.qsize() > 0:
        now_node = pq.get()
        
        now = now_node[1]
        if not visit[now]:
            visit[now] =True
            
            for n in board[now]:
                if not visit[n[0]] and route[n[0]] > route[now] +n[1]:
                    # print(n[0])
                    route[n[0]] = route[now] + n[1]
                    pq.put((route[now]+n[1], n[0]))
    # print(route[end])
    return route[end]

print(dijkstra(start_index, end_index))