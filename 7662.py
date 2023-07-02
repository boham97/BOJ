from heapq import heappush, heappop

T = int(input())
for _ in range(T):
    k = int(input())

    arr = [0] *(k)
    iq = []
    dq = []

    for i in range(k):
        a, s =  input().split()
        s = int(s)
        if a == 'I':
            heappush(iq, (-s, i))
            heappush(dq, (s,i))
        else:
            if s == 1:
                if iq and not arr[iq[0][1]]:
                    arr[iq[0][1]] = 1
            else:
                if iq and not arr[iq[0][1]]:
                    arr[dq[0][1]] = 1
                    
        while iq and arr[iq[0][1]]:
            heappop(iq)
        while dq and arr[dq[0][1]]:
            heappop(dq)

    if iq:
        print(-iq[0][0], dq[0][0])
    else:
        print('EMPTY')
