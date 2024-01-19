n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, sum(trees)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for tree in trees:
        if tree > mid:
            cnt += tree - mid
    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)

# #중간값을 찾아서 그것의 최댓값을 구하는 문제임
# n, m = map(int, input().split())
# # 나무들의 리스트
# trees = list(map(int, input().split())) 

# start, end =1, sum(trees)

# while start <= end:
#     mid = (start + end) // 2
#     cnt = 0
    
#     for tree in trees:
#         if tree > mid:
#             cnt += tree - mid
#         if cnt >= m:
#             start = mid + 1
#         else: end = mid - 1
# print(end)

