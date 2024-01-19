import sys
n =int(sys.stdin.readline())
inputs = []

for _ in range(n):
    inputs.append(input().split())
class Node():
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

def pre_order(node):
    print(node.item, end='')
    if node.left != '.':
        pre_order((tree[node.left]))
    if node.right != '.':
        pre_order((tree[node.right]))

def in_order(node):
    
    if node.left != '.':
        pre_order((tree[node.left]))
    print(node.item, end='')
    if node.right != '.':
        pre_order((tree[node.right]))

def post_order(node):
    if node.left != '.':
        pre_order((tree[node.left]))    
    if node.right != '.':
        pre_order((tree[node.right]))
    print(node.item, end='')

tree = {}
for item, left, right in inputs:
    tree[item] = Node(item, left, right)
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
