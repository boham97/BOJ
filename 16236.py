N = int(input())
size = 2
eaten_fish = 0
arr = [0] *N
for i in range(N):
    arr[i] = list(map(int, input().split()))
logic = 5
ans = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            shark = [i, j]
            arr[i][j] = 0

while logic:
    breaker = 0
    targets = list()
    for i in range(N):
        for j in range(N):
            if 0 < arr[i][j] < size:
                targets.append([abs(shark[0] - i)+abs(shark[1] - j), i, j])
    targets.sort()
    if len(targets) == 0:
        break
    for fish in targets:
        move = range(fish[0])
        if breaker == 1:
            break
        for i in range(1 << fish[0]):
            cnt = 0
            up = list()
            for j in range(fish[0]):
                if i & (1 << j):
                    cnt += 1
                    up.append(j)
            if cnt == abs(shark[0] - fish[1]):
                temp_pos = [shark[0], shark[1]]
                for j in range(fish[0]):
                    if j in up:
                        temp_pos[0] += int((fish[1] - shark[0])/abs(fish[1] - shark[0]))
                        if arr[temp_pos[0]][temp_pos[1]] > size:
                            break
                    else:
                        temp_pos[1] += int((fish[2] - shark[1]) / abs(fish[2] - shark[1]))
                        if arr[temp_pos[0]][temp_pos[1]] > size:
                            break
                else:
                    shark = [temp_pos[0], temp_pos[1]]
                    arr[temp_pos[0]][temp_pos[1]] = 0
                    eaten_fish += 1
                    ans += fish[0]
                    breaker = 1
                    if eaten_fish == size:
                        size += 1
                        eaten_fish = 0

    print()

print(ans)
