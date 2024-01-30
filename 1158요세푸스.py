import sys
input = sys.stdin.readline


def josephus(n, k):
    people = list(range(1, n + 1))
    result = []

    index = 0
    while people:
        index = (index + k - 1) % len(people)
        
        result.append(people.pop(index))

    return result

# 예제 사용
n, k = map(int, input().split())

# 요세푸스 문제 풀이
sequence = josephus(n, k)
print("<{}>".format(', '.join(map(str, sequence))))
