def func(temp):
    global N

    if len(temp) == 0:
        for i in arr:
            temp.append(i)
            func(temp)
            temp.pop()
    elif len(temp) < N:
        for i in arr:
            if i >= temp[-1]:
                temp.append(i)
                func(temp)
                temp.pop()
    else:
        print(*temp)

M, N = map(int, input().split())

arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()

func([])

