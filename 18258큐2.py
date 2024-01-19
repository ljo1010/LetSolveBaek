#소문자로 받아야함 
# 그래서 받을 때 .lower()를 써줘야함
import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0].lower() == 'push':
        b = int(command[i])
        queue.append(b)
    elif command[0].lower() == 'pop':
        if not queue:
            print(-1)
        else:
           front_element = queue.popleft()
           print(front_element)    
    elif command[0].lower() == 'size':
        print(len(queue))
    elif command[0].lower() == 'empty':
        if not queue:
            print(-1)
        else:          
           print(0)
    elif command[0].lower() == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command[0].lower() == 'back':
        if not queue: # 큐가 아닐시로 가정 라이브러리 가져왔으면 쓰자
            print(-1)
        else:
            back_element = queue[-1]
            print(back_element)