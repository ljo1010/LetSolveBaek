import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
a = list(input())
a.pop()
b = list(input())
b.pop()
dp = [[0 for j in range(len(b)+1)]for i in range(len(a)+1)]
path = []

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[len(a)][len(b)])

def get_text(r, c):
    if r ==0 or c==0:
        return
    if a[r-1] == b[c-1]:
        path.append(a[r-1])
        get_text(r-1, c-1)
    else:
        if dp[r-1][c]>dp[r][c-1]:
            get_text(r-1, c)
        else:
            get_text(r, c-1)

get_text(len(a), len(b))

for i in range(len(path)-1, -1, -1):
    print(path.pop(i), end='')

print()