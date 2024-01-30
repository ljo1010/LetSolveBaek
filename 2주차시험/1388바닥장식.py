import sys
input = sys.stdin.readline

#n은 세로 m은 가로
n,m = map(int, input().split()) 
#2차원 배열저장
floor = []

for _ in range(n):
    floor.append(list(input()))

#dfs방식으로 문제를 접근
#조건만 추가하면 되기 때문
#조건은 -일때와 |일 떄 새로운 값을 만들어 더하게 하는 로직
def dfs(x,y):

    if floor[x][y] == '|':
        floor[x][y] = 1	   
        for b in [1,-1]: 
            new_x = x + b  
            if (new_x > 0 and new_x < n) and floor[new_x][y] == '|':
                dfs(new_x,y)

    if floor[x][y] == '-':
        floor[x][y] = 1	   
        for a in [1,-1]:  
            new_y = y + a
            if (new_y > 0 and new_y < m) and floor[x][new_y] == '-':
                dfs(x,new_y)
  
count = 0
for i in range(n):
    for j in range(m):
        if floor[i][j] == '-' or floor[i][j] == '|':
            dfs(i,j) 
            count += 1

print(count)