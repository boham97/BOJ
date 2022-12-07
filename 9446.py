tc = int(input())
for test in range(tc):
    N = int(input())
    arr = list(map(int,input().split()))
    arr.insert(0,0)
    visit = [0]* len(arr)
    ans = 0
    for i in range(len(arr)):
        if visit[i] == 0:
            temp = [i]
            visit[i] = 1
            while not visit[arr[temp[-1]]]:
                visit[arr[temp[-1]]] = 1
                temp.append(arr[temp[-1]])
            temp.append(arr[temp[-1]])
            index = temp.index(temp[-1])
            ans += index
    print(ans)