class ListStack:
    
    def __init__(self) -> None:
        self.__stack = []
    
    def push(self, x):
        self.__stack.append(x)

    def pop(self):
        self.__stack.pop()
    
    def size(self):
        self.__stack.size()

    def empty(self):
        return not bool(self.__stack)

    def top(self):
        if self.empty():
            return None
        else:
            return self.__stack[-1]
        
n = int(input())
for i in range(n):
    commend = str(input())