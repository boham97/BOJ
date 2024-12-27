def hanoi(a, b, c):
    if a == 1:
        print(b, c)
    else:
        hanoi(a - 1, b, 6 - b - c)
        hanoi(1, b, c)
        hanoi(a - 1, 6 - b - c, c)

n = int(input())
print(2**n -1)
if n <= 20:
    hanoi(n, 1, 3)
