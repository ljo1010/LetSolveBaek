import sys
a, b, v = map(int, sys.stdin.readline().split())
print((v-b) % (a-b))
