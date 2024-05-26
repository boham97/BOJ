import sys
input = sys.stdin.readline

def dfs(i, j, target, hap):
    if i == j:
        if hap in  target:
            target[hap] = target[hap] + 1
        else:
            target[hap] = 1
        return
    dfs( i + 1, j, target, hap + arr[i])
    dfs( i + 1, j, target, hap)
        
def print_ans():
    ans = 0
    for i in left:
        if s - i in right:
            ans += left[i] *right[s-i]
    print(ans if s else ans - 1)




n, s = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
left, right = dict(), dict()
dfs(0, len(arr)// 2 + 1, left, 0)
dfs(len(arr)// 2 + 1, len(arr), right, 0)
print_ans()
