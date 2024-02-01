'''
뭔가 회의실 문제와 멀티탭 문제를 합친 것 같다라는 생각을 했음.
시작시간이 있고 끝 시간이 있는것 그리고 최소한의 강의실을 배정해야한다는 것.
'''

import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    num, start, end = list(map(int, input().split()))
