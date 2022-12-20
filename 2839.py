N = int(input())
for i in [0,3,6,9,12]:
    if N-i > 0 and (N-i)%5 == 0:
        ans =(N-i)//5 +i//3
        print(ans)
        break
else:
    if N%3 == 0:
        print(N//3)
    else:
        print(-1)
