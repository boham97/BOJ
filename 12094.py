from pprint import pprint


def dfs(n,arr):
    global ans
    if n == 10:
        return
    else:
        logic = 0
        next = [[0]* N for _ in range(N)]
        for i in range(N):
            temp = []
            for j in range(N):
                if arr[i][j]  > 0:
                    temp.append(arr[i][j])
            if len(temp) > 1:
                for k in range(1,len(temp)):
                    if temp[k-1] == temp[k]:
                        temp[k-1] *= 2
                        temp[k] = 0
                nextpos = 0
                for k in temp:
                    if k:
                        next[i][nextpos] = k
                        nextpos += 1
            if arr[i] == next[i]:
                logic += 1
        if logic != N:
            pprint(next)
            dfs(n+1,next)
        logic = 0
        next = [[0]* N for _ in range(N)]
        for i in range(N):
            temp = []
            for j in range(N-1,-1-1):
                if arr[i][j]  > 0:
                    temp.append(arr[i][j])
            print(temp)
            if len(temp) > 1:
                for k in range(len(temp)-1,0,-1):
                    if temp[k-1] == temp[k]:
                        temp[k] *= 2
                        temp[k-1] = 0
                nextpos = N-1
                for k in temp[::-1]:
                    if k:
                        next[i][nextpos] = k
                        nextpos -= 1
            if arr[i] == next[i]:
                logic += 1
        if logic != N:
            pprint(next)
            dfs(n+1,next)



N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 2
dfs(0,arr)