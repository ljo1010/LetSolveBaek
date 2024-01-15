# import sys
# input = sys.stdin.readline

# n = int(input())
# lis = []

# for i in range(n):
#     lis.append(int(input()))
 
# for i in range(lis):
#     print(i)
# 위에거는 라이브러리를 가지고 와서 시간을 줄여주는 방식이나 지양해야 할듯함.
import sys
input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

def sort(arr):
    if len(arr) < 2:
        return arr # 이걸 리턴하는 이유는 길이가 1일때는 정렬 못한다.

    mid = len(arr)//2
    left = sort(arr[:mid])
    right = sort(arr[mid:])

    return merge(left, right)#재귀방식임.

def merge(left, right):
    new_list = []
    i = 0
    j = 0

    while (i < len(left)) & (j < len(right)):
        if left[i] > right[j]:
            new_list.append(right[j])
            j += 1
        else:
            new_list.append(left[i])
            i += 1
    while(j < len(right)):
        new_list.append(right[j])
    while(i < len(left)):
        new_list.append(left[i])
        i += 1
    return new_list

for i in sort(li):
    print(i)  