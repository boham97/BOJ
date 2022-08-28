tc = int(input())
for test in range(tc):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    apoint = [0] * 5
    bpoint = [0] * 5
    for i in a[1:]:
        apoint[i] +=1
    for i in b[1:]:
        bpoint[i] +=1
    for i in range(4,0,-1):
        if apoint[i] > bpoint[i]:
            print('A')
            break
        elif apoint[i] < bpoint[i]:
            print('B')
            break
    else:
        print('D')