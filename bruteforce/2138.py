def dfs(index):
    if index == N:
        cal()
        return
    for i in range(3):
        ans[index] = i
        dfs(index + 1)

def cal():
    last = N
    hap = 0
    combo = 1
    for i in range(N - 1, -1, -1):
        if ans[i] == 1:
            hap += last
            last = i
            combo = 1
        elif ans[i] == 2:
            hap -= last
            last = i
            combo = 1
        else:
            last = last + 10 ** combo * i
            combo += 1
    if (hap + last) ==0:
        printAns()

def printAns():
    for i in range(N - 1):
        print(i + 1, end= '')
        print('+' if ans[i + 1] == 1 else ('-' if ans[i + 1] == 2 else ' '), end ='')
    print(N)
    
for _ in range(int(input())):
    N = int(input())
    ans = [0] * N
    dfs(1)
    print()
