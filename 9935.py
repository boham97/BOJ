arr = list(input())
temp = list(input())
collect = len(temp)

ans = []

for i in range(len(arr)):

    ans.append(arr[i])
    if arr[i] == temp[-1] and len(ans) >= collect:
        for j in range(collect):
            if ans[(-1-j)] != temp[(-1-j)] : 
                break
        else:
            for _ in range(collect):
                ans.pop()


print(''.join(ans)) if len(ans) > 0 else print("FRULA")
