# import sys
# import heapq
# n = int(input())
# heap = []

# for i in range(n):
#     a = int(sys.stdin.readline())
#     if a == 0:
#         if heap:
#             print((-1)*heapq.heappop(heap))
#         else:
#             print(0)
#     else:
#         heapq.heappush(heap, (-1)*a)

import sys
from queue import PriorityQueue

input = sys.stdin.readline
n = int(input())
pq = PriorityQueue()

for _ in range(n):
    a = (int(input()))
    if a == 0:
        if pq:
            print(a)
        else:
            print(0)
    else:
        PriorityQueue.put(a)