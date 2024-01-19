import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0].lower() == 'push':
        b = int(command[1])
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
            print(1)
        else:
            print(0)
    elif command[0].lower() == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command[0].lower() == 'back':
        if not queue:
            print(-1)
        else:
            back_element = queue[-1]
            print(back_element)
