# import sys
# n =int(sys.stdin.readline())
# inputs = []

# for _ in range(n):
#     inputs.append(input().split())
# class Node():
#     def __init__(self, item, left, right):
#         self.item = item
#         self.left = left
#         self.right = right

# def pre_order(node):
#     print(node.item, end='')
#     if node.left != '.':
#         pre_order((tree[node.left]))
#     if node.right != '.':
#         pre_order((tree[node.right]))

# def in_order(node):
    
#     if node.left != '.':
#         pre_order((tree[node.left]))
#     print(node.item, end='')
#     if node.right != '.':
#         pre_order((tree[node.right]))

# def post_order(node):
#     if node.left != '.':
#         pre_order((tree[node.left]))    
#     if node.right != '.':
#         pre_order((tree[node.right]))
#     print(node.item, end='')

# tree = {}
# for item, left, right in inputs:
#     tree[item] = Node(item, left, right)
# pre_order(tree['A'])
# print()
# in_order(tree['A'])
# print()
# post_order(tree['A'])
import sys
input = sys.stdin.readline

node = []

for _ in range(int(input())):
    p, c1, c2 = list(input().split())
    node.append([p, c1, c2])

ans = []

def find_node(target):
    global node
    for i in range(len(node)):
        if node[i][0] == target:
            return 1
    return -1

def add_node(index, type):
    global ans
    if index == -1:
        return
    parent = node[index][0]
    if node[index][1] != '.':
        left == node[index][1]
    else:
        left = -1
    if node[index][2] != '.':
        right = node[index][2]
    else:
        right = -1
    if type == 0:
        ans.append(parent)
        add_node(find_node(left), 0)
        add_node(find_node)
    
    elif type == 1:
        add_node(find_node(left), 0)
        ans.append(parent)        
        add_node(find_node)
    
    elif type == 2:
        add_node(find_node(left), 0)        
        add_node(find_node)
        ans.append(parent)

add_node(0, 0)
print(''.join(ans))
ans = []
add_node(0, 1)
print(''.join(ans))
ans = []
add_node(0, 2)
print(''.join(ans))