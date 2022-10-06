def fibonacci6(n):
    if n < 2:
        return n
    elif n in fibo:
        return fibo[n]
    else:
        if n%2 == 0:
            temp = ((fibonacci6(n//2)**2) +2*(fibonacci6(n//2)*fibonacci6(n//2-1)))%D
            fibo[n] = temp
            return temp
        else:
            temp =((fibonacci6(n//2)**2) + (fibonacci6(n//2+1)**2))%D
            fibo[n] = temp
            return temp

            
n = int(input())
fibo = {
    0: 0,
    1: 1,
}
D = 1000000007
print(fibonacci6(n))