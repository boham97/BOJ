def dfs(i):
    global ans
    if len(bishop)+(2*N-1-i) <= ans:
        return
    if ans == 2*N-2:
        return
    if i == 2*N-1:
        if ans < len(bishop):
            ans =len(bishop)
        return
    else:
        temp = 1
        for j in range(i+1):
            if i-j<N and j<N and arr[i-j][j] == 1:
                for x,y in bishop:
                    if abs(x-i+j)==abs(j-y):
                        break
                else:
                    bishop.append([i-j, j])
                    dfs(i+1)
                    temp =0
                    bishop.pop()
        if temp:
            dfs(i+1)  


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
bishop = []
ans = 0
dfs(0)

    
print(ans)