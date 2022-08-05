import itertools

N, M, D = list(map(int,input().split()))
arr = [[] for i in range(N)]
for i in range(N):
    arr[i] = list(map(int,input().split()))
max_cnt = 0

for archers in itertools.combinations(range(M), 3):
    #print(archers)
    cnt = 0
    enemy = [[] for i in range(N)]
    for i in range(N):
        enemy[i] = arr[i][:]
    while(1):
        targets = []
        B = len(enemy)
        for archer in archers:
            target=[]
            for j in range(B):
                for k in range(M):
                    dist = abs(B-j) + abs(k-archer)
                    if enemy[j][k] == 1 and dist <= D:
                        target.append([dist, k, j])
            target.sort()
            if target != []:
                targets.append(target[0])
        for attack_target in targets:
            if enemy[attack_target[2]][attack_target[1]] == 1:
                cnt += 1
                enemy[attack_target[2]][attack_target[1]] = 0
        enemy.pop()
        if enemy ==[]:
            break
    if cnt > max_cnt:
        max_cnt = cnt
print(max_cnt)