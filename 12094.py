def dfs(n,arr, string2 = ''):
    global ans
    temp = 0
    #print(arr, n,string2)
    for i in range(N):
        temp = max(temp, max(arr[i]))
    if temp > ans:
        ans = temp
    if n == 10:
        return
    else:
        string = ''
        for i in range(N):
            for j in range(N):
                string += str(arr[i][j])
        if string in memo and memo[string] < n:
            return
        else:
            memo[string] = n
        logic = 0
        next = [[0]* N for _ in range(N)]
        for i in range(N):
            temp = []
            for j in range(N):
                if arr[i][j]  > 0:
                    temp.append(arr[i][j])
            if len(temp) > 0:
                for k in range(1,len(temp)):
                    if temp[k-1] == temp[k]:
                        temp[k-1] <<=1
                        temp[k] = 0
                nextpos = 0
                for k in temp:
                    if k:
                        next[i][nextpos] = k
                        nextpos += 1
            if arr[i] == next[i]:
                logic += 1
        if logic != N:
            dfs(n+1,next, string2 +'1')

        logic = 0
        next = [[0]* N for _ in range(N)]
        for i in range(N):
            temp = []
            for j in range(N-1, -1, -1):
                if arr[i][j]  > 0:
                    temp.append(arr[i][j])
            if len(temp) > 0:
                for k in range(1,len(temp)):
                    if temp[k-1] == temp[k]:
                        temp[k-1] <<= 1
                        temp[k] = 0
                nextpos = N-1
                for k in temp:
                    if k:
                        next[i][nextpos] = k
                        nextpos -= 1
            if arr[i] == next[i]:
                logic += 1
        if logic != N:
            dfs(n+1,next, string2+'2')
        
        logic = 0
        next = [[0]* N for _ in range(N)]
        for i in range(N):
            temp = []
            for j in range(N):
                if arr[j][i]  > 0:
                    temp.append(arr[j][i])
            if len(temp) > 0:
                for k in range(1,len(temp)):
                    if temp[k-1] == temp[k]:
                        temp[k-1] <<= 1
                        temp[k] = 0
                nextpos = 0
                for k in temp:
                    if k:
                        next[nextpos][i] = k
                        nextpos += 1
            for j in range(N):
                if arr[j][i] != next[j][i]:
                    break
            else:
                logic += 1
        if logic != N:
            dfs(n+1,next,string2 +'3')

        logic = 0
        next = [[0]* N for _ in range(N)]
        for i in range(N):
            temp = []
            for j in range(N-1, -1, -1):
                if arr[j][i]  > 0:
                    temp.append(arr[j][i])
            if len(temp) > 0:
                for k in range(1,len(temp)):
                    if temp[k-1] == temp[k]:
                        temp[k-1] <<= 1
                        temp[k] = 0
                nextpos = N-1
                for k in temp:
                    if k:
                        next[nextpos][i] = k
                        nextpos -= 1
            for j in range(N):
                if arr[j][i] != next[j][i]:
                    break
            else:
                logic += 1
        if logic != N:
            dfs(n+1,next, string2+'4')



N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
memo = {}
ans = 2
dfs(0,arr)
print(ans)
print(memo)