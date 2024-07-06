def calculate_lcm(n):
    arr = [True] * int((n+1)//2) #소수는 2를 제외하면 홀수니까 반으로 줄여보자
    arr[0]= False
    
    for i in range(int((n + 1)**0.5)//2 + 1):
        if arr[i]:
            for j in range(3 * i + 1, (n+1)//2, i * 2 + 1):
                arr[j] = False
    ans = 1
    mod = 2**32
    
    for i in range((n+1)//2):
        if arr[i]:
            now = i * 2 + 1
            while now * ( i * 2 + 1) <= n:
                now *= i * 2 + 1      
            ans = (ans * now) % mod

            
    now = 2
    while now * 2 <= n:
        now *= 2
    ans = (ans * now) % mod
    return ans


n = int(input())
print(calculate_lcm(n))
