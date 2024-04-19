def get_gcd(x, y):
    while y != 0:
        t = x%y
        x, y = y, t
    return abs(x)

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    arr = list(map(int, input().split()))
    gcd = arr[1]
    for i in arr[2:]:
        gcd = get_gcd(gcd, i)

    if x%gcd or y%gcd:
        print("Gave up")
    else:
        print("Ta-da")
    
