import sys

T = int(input())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    sys.stdout.write(A + B)
