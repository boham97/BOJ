def solution(arr, l, r):
    ans1 = 0
    cnt = 1

    for i in arr:
        a, b = min(r, cnt + i - 1), max(l, cnt)
        if a >= b:
            ans1 += i * (1 + a - b)

        cnt += i

    temp = 0
    k = 0
    for i in arr:
        if k == r - l + 1:
            break
        index = min(r - l + 1, i)
        temp += index * i
        k += index
        print(i, index, temp)
    return [ans1, 0]


