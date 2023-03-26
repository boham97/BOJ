def func(temp):
    if not len(temp):
        for i in arr:
            func([i])
    elif len(temp) < M:
        for i in arr:
            if i >= temp[-1]:
                temp.append(i)
                func(temp)
                temp.pop()
    else:
        print(*temp)


N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

func([])