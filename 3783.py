from decimal import Decimal, getcontext, ROUND_DOWN

getcontext().prec = 300

def bs():
    n = Decimal(input())
    cnt= 0
    left, right = Decimal(0), Decimal(10**50)
    mid = (left +right) / 2
    gap = Decimal(1e-11)
    while abs(n - (mid ** 3)) > gap and cnt < 700:
        if mid ** 3 > n:
            right = mid
        else:
            left = mid
        mid = (left + right) /2
        cnt += 1
        if cnt%100 == 0: print(n - mid**3, cnt)
    return mid


t = int(input())

for _ in range(t):
    ans = bs().quantize(Decimal('1.0000000000'), ROUND_DOWN)
    print(ans)
######################################
from decimal import Decimal, getcontext, ROUND_DOWN

getcontext().prec = 1000
    
   
def bs(n):
    n = Decimal(n + '.0000000000')
    pow = Decimal('1') / Decimal('3')
    ans = Decimal(n ** pow)
    ans = round(ans, 500)
    ans = Decimal(ans).quantize(Decimal('.0000000001'), rounding=ROUND_DOWN)
    return ans


t = int(input())

for _ in range(t):
    ans = bs(input().rstrip())
    print(ans)





