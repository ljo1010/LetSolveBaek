class Node():
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

def pre_order(node):
    print(node.item, end='')
    