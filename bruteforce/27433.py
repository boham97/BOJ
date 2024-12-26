def p(n):
    return n*p(n - 1) if n else 1
print(p(int(input())))
