import sys
input = sys.stdin.readline
ans = 0
n = int(input())
arr = list(map(int, input().split()))

arr.sort()
#print(arr)

for i in range(n - 2):
    l, r = i + 1, n -1
    while l < r:
        hap = arr[l] + arr[r] + arr[i]
        if hap == 0:
            if arr[l] == arr[r]:
                ans += (r - l + 1) * (r - l) /2
                break
            else:
                l_combo = 1
                while arr[l] == arr[l + 1]:
                    l_combo += 1
                    l += 1
                r_combo = 1
                while arr[r] == arr[r - 1]:
                    r_combo += 1        
                    r -= 1
                ans += r_combo * l_combo
                l += 1
        elif hap > 0:
            r -= 1
        else:
            l += 1            

print(int(ans))
