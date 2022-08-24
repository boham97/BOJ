tc = int(input())
for test in range(tc):
    N, M = list(map(int, input().split()))
    arr = [0] * N
    for i in range(N):
        arr[i] = list(input())
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cross = []
    point = []
    ans = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 's':
                s_pos = [i, j]
            elif arr[i][j] == 't':
                t_pos = [i, j]

    for i in range(1,N-1):
        for j in range(1,M-1):
            cnt1 = 0
            cnt2 = 0
            for k in range(4):
                if arr[i +dx[k]][j+dy[k]] == '#':
                    cnt1 += 1
                elif arr[i +dx[k]][j+dy[k]] == '.' or arr[i +dx[k]][j+dy[k]] == 's' or arr[i +dx[k]][j+dy[k]] == 't':
                    cnt2 += 1
            if cnt1 == 3:
                point.append([i, j])
            if cnt2 >= 3:
                cross.append([i, j])
                cross.append(cnt2 - 1)


    stack = [s_pos]
    visited = [s_pos]
    top = 0
    while stack:
        for i in range(4):
            if 0 <= stack[top][0]+dx[i] < N and 0 <= stack[top][1]+dy[i] < M and arr[stack[top][0] + dx[i]][stack[top][1] + dy[i]] != '#' and [stack[top][0] + dx[i], stack[top][1] + dy[i]] not in visited:
                stack.append([stack[top][0] + dx[i], stack[top][1] + dy[i]])
                visited.append([stack[top][0] + dx[i], stack[top][1] + dy[i]])
                top += 1
                break
        else:
            temp = 0
            if [i for i in stack if i in point] or t_pos in stack:
                temp = len(stack) - 1
                for i in stack:
                    if i in cross:
                        temp = temp /(cross[cross.index(i)+1])
            ans += temp
            top -= 1
            stack.pop()

    
    print(ans)