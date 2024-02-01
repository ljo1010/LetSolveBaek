'''
계단오르기의 규칙들
계단은 한번에 한 계단 두 계단씩 오를 수 있다. 
연속된 세계를 밟으면 안된다.
첫번째 계단을 오르거나 두번째 계단을 오를 때까지는 다 더해서 출력하면 된다 
세번째 부터는 어떤 계단을 가야 최대값이 되는지 생각해 보면 될 것처럼 보인다.
점화식은 첫번째 계단을 오르고 나서 그 다음 계단을 계속 오르거나 두번째 계단을 올랐을 때의 값을 비교해서
그것들의 최댓값을 비교해서 max로 구하면 된다. 
바텀업 방식으로 풂.
그러면 점화식은 이렇게 나온다.
max(d[i-3]+stair[i-1]+stair[i], d[i-2]+stair[i])
'''
import sys
input = sys.stdin.readline

n = int(input())

stair = [0] * 301
for i in range(1, n+1):
    stair[i] =int(input())

d = [0]*301
d[1] =stair[1]
d[2] =stair[1]+stair[2]
# d[3] =max(stair[1] + stair[3], stair[2]+stair[3])
for i in range(3, n+1):
    d[i] =max(d[i-3]+stair[i-1]+stair[i], d[i-2]+stair[i])

print(d[n])
