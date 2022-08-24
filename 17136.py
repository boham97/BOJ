def judging(i, j, c):
    cnt = 0
    for m in range(c):
        for n in range(c):
            if counted[i+m][j+n] == 0:
                cnt += arr[i+m][j+n]
    if cnt == c*c:
        return c
    else:
        return judging(i, j, c-1)


def counting(i, j, c):
    for m in range(c):
        for n in range(c):
            counted[i+m][j+n] = 1


def uncounting(i, j, c):
    for m in range(c):
        for n in range(c):
            counted[i+m][j+n] = 0


arr = [list(map(int, input().split())) for _ in range(10)]
for i in range(10):
    for j in range(4):
        arr[i].append(0)
for i in range(5):
    arr.append([0]*14)
count_1 = 0
for i in range(10):
    for j in range(10):
        if arr[i][j]:
            count_1 += 1
ans = count_1
stack_pos = []
stack_size = [0]
counted = [[0] * 14 for _ in range(15)]
while stack_size:
    logic1 = 0
    logic2 = 0
    for i in range(11):
        if logic2 == 1:
            continue
        if logic1 == 1:
            break
        for j in range(10):
            if arr[i][j] == 1 and counted[i][j] == 0:
                stack_pos.append([i, j])
                stack_size.append(judging(i, j, 5))
                counting(i, j, stack_size[-1])
                for k in range(1, 6):
                    if stack_size.count(k) > 5:
                        logic2 = 1
                        break
                if len(stack_size) > ans:
                    logic2 = 1
                    break
                logic1 = 1
                break
    else:
        temp = 0
        for i in range(10):
            temp += sum(counted[i])
        if len(stack_size)-1 <= ans and temp == count_1 and logic2 == 0:
            ans = len(stack_size) - 1
        while logic2:
            uncounting(stack_pos[-1][0], stack_pos[-1][1], stack_size[-1])
            stack_size.pop()
            stack_pos.pop()
            for i in range(1, 6):
                if stack_size.count(i) > 5:
                    logic2 = 1
                    break
            else:
                logic2 = 0
        while stack_size[-1] == 1 and len(stack_size) > 1:
            uncounting(stack_pos[-1][0], stack_pos[-1][1], stack_size[-1])
            stack_size.pop()
            stack_pos.pop()
        else:
            if len(stack_size)-1:
                uncounting(stack_pos[-1][0], stack_pos[-1][1], stack_size[-1])
                stack_size[-1] -= 1
                counting(stack_pos[-1][0], stack_pos[-1][1], stack_size[-1])
        if stack_size[-1] == 0:
            stack_size.pop()
            break

if ans == count_1 and ans > 5:
    print(-1)
else:
    print(ans)