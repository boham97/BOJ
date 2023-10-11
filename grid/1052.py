n, k = map(int, input().split())

num = n

while bin(n).count('1') > k:
    idx = bin(n)[::-1].index('1')
    n += 2**idx


print(n - num)
