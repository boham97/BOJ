def find():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    arr.sort()
    ans = 0
    left = set()
    for i in range(n):
        for j in range(n):
            left.add(arr[i] + arr[j])

    for i in range(n -1, 0, -1):
        for j in range(i):
            if arr[i] - arr[j] in left:
                print(arr[i])
                return

find()
