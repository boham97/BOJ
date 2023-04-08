T = int(input())
for _ in range(T):
    N = int(input())
    ans = [0] * (1+N)
    tree = [0] * (1+N)

    for _ in range(N-1):
        A, B = map(int, input().split())
        tree[B] = A
    num1, num2 = map(int, input().split())

    while 1:
        if num1 == 0:
            break

        ans[num1] = 1
        num1 = tree[num1]
    
    while 1:
        if ans[num2] == 1:
            res = num2
            break
        else:
            num2 = tree[num2]
    
    print(res)
