from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())

    logic = True
    temp = list(map(int, input().split()))
    arr = [[] for _ in range(N+1)]
    income = [0] * (N+1)

    for i in range(N):
        for j in range(i + 1, N):
            arr[temp[i]].append(temp[j])
            income[temp[j]] += 1
            
    M = int(input())
    for _ in range(M):
        a, b = map(int,input().split())
        if b in arr[a]:
            arr[b].append(a)
            income[a] += 1
            arr[a].remove(b)
            income[b] -= 1
        else:
            arr[a].append(b)
            income[b] += 1
            arr[b].remove(a)
            income[a] -= 1
    ans = []
    que = deque()
    for i in temp:
        if income[i] == 0:
            que.append(i)
        
    while que:
        if len(que) > 1:
            logic = False
            break
        now = que.popleft()
        ans.append(now)
        for i in arr[now]:
            income[i] -= 1
            if income[i] == 0:
                que.append(i)
    if len(ans) == N and logic:
        print(* ans)
    else:
        print("IMPOSSIBLE")
