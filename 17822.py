import pprint
N, M, T = list(map(int,input().split()))

arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

order_arr = []
for t in range(T):
    order_arr.append(list(map(int, input().split())))

for turn in range(T):
    r, cw, time = order_arr[turn][:]
    for i in range(r-1, N, r):
        for j in range((1-cw)*(time%4)+cw*(4-time%4)):
            temp = arr[i].pop()
            arr[i].insert(0, temp)
    pprint.pprint(arr)
temp = []

for i in range(10)
