import sys

def star(N):
    for i in range(2*N-1):
        if arr[i]:
            print("*", end="")
        else:
            print(' ', end= "")
    print()

N = int(input())

arr = [0] * (2*N - 1)
arr[N-1] = 1
star(N)
for _ in range(N-1):
    next = [0] * (2*N - 1)
    for i in range(2*N-1):
        if arr[i] == 1:
            next[i-1] = 2
            next[i+1] = 6
        elif arr[i] == 2:
            next[i-1] = 3
            next[i] = 4
            next[i+1] = 5
        elif arr[i] == 6:
            next[i-1] = 5
            next[i] = 7
            next[i+1] = 8
        elif arr[i] == 3:
            if next[i-1]:
                next[i - 1] = 0
            else:
                next[i-1] = 1
        elif arr[i] == 8:
            next[i+1] = 1
    arr = next[::]
    star(N)