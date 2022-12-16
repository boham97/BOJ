def cal(x,y,c,z):
    temp = ((x**2-z**2)**0.5-c)*((y**2-z**2)**0.5-c)-c**2
    return temp


x,y,c = map(float, input().split())
start = 0
end = min(x,y)

while start < end:
    mid = (start + end)/2
    temp = cal(x,y,c,mid)
    if abs(temp) <0.01:
        break
    elif temp > 0:
        start = mid
    elif temp < 0:
        end = mid

print(mid)
