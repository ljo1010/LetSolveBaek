A = int(input())
data = []

for i in range(A):
    data.append(int(input()))

for i in range(0, A-1):
    for j in range(0, A-1-i):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

for i in range(A):
    print(data[i])