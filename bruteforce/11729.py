def hanoi(a, b, c, d):
    if a == 1:
        print(b, c)
    else:
        hanoi(a - 1, b,d, c)
        hanoi(1, b, c ,d)
        hanoi(a - 1, d, c, b)

n = int(input())
print(2**n -1)
hanoi(n, 1, 3, 2)
