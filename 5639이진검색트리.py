# import sys
# sys.setrecursionlimit(10**9)

# input = sys.stdin.readline

# pre_arr = []

# while True:
#     try:
#         num = int(input())
#         pre_arr.append(num)
#     except:
#         break

# def post_order(root_index, end_index):
#     if root_index > end_index:
#         return
    
#     global pre_arr

#     right_start = end_index + 1

#     for i in range(root_index + 1, end_index + 1):
#         if pre_arr[root_index] < pre_arr[i]:
#             right_start = 1
#             break
    
#     post_order(root_index + 1, right_start - 1)
#     post_order(right_start, end_index)

#     print(pre_arr[root_index])

# post_order(0, len(pre_arr) -1)

import sys
sys.setrecursionlimit(10**6)
num_list = []
while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break

def postorder(first,end):
    if first > end:
        return
    mid = end+1   # 루트보다 큰 값이 존재하지 않을 경우를 대비   
    for i in range(first+1,end+1):
        if num_list[first] < num_list[i]:
            mid = i
            break
    
    postorder(first+1, mid-1)
    postorder(mid, end)
    print(num_list[first])

postorder(0,len(num_list)-1)