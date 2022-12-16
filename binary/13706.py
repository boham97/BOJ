N = int(input())

start = 1
end = N//2

while start <= end:
    mid = (start + end)// 2
    temp = mid **2
    if temp < N:
        start = mid + 1
    elif temp > N:
        end = mid - 1
    else:
        break 
    print(mid)