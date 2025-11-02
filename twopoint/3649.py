while 1:
    try :
        x = int(input()) * 10000000
    except : break
    
    n = int(input())
    
    arr = [0] * n
    for i in range(n):
        arr[i] = int(input())
        
    arr.sort()
    
    i, j = 0, n - 1
    
    ans = None
    while i < j:
        temp = arr[i] + arr[j]
    
        if temp < x:
            i += 1
        elif temp > x:
            j -= 1
        else:
            ans = (arr[i], arr[j])
            break
    print('danger' if ans is None else f'yes {ans[0]} {ans[1]}')