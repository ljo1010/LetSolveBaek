'''
문제 이름 이친수
1과 0으로 이뤄진 이진수 ! 이진수의 특별한 성질을 가진 수를 이친수 라고 한다.
1. 이친수는 0으로 시작하지 않는다.
2. 이친수는 1이 두 번 연속으로 나타나지 않는다. 11을 부분 문자열로 갖지 않는다. 
예제 3을 넣을 시 2를 출력
'''
n = list(map(int, input().split()))

for i in range(n):
    