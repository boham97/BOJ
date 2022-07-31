import itertools

ining = int(input())
hitter = [[0 for i in range(ining)] for j in range(9)]
temp =[[] for i in range(ining)]
for i in range(ining):
    temp[i] = list(map(int, input().split()))

for i in range(9):
    for j in range(ining):
        hitter[i][j] = temp[j][i]
max_point = 0
for hit_infor in itertools.permutations(hitter[1:], 8):
    hit_infor = list(hit_infor)
    hit_infor.insert(3, hitter[0])
    point = 0
    hitter_num = 0
    for attack_ining in range(ining):
        out_count = 0
        runner = [0, 0, 0]
        hit_history =[]
        while(out_count < 3):
            if hit_infor[hitter_num][attack_ining] == 0:
                out_count += 1
            else:
                hit_history.append(hit_infor[hitter_num][attack_ining])
            hitter_num += 1
            hitter_num = hitter_num % 9
        left =0
        cnt = 0
        for i in hit_history[::-1]:
            left += i
            cnt += 1
            if left >3:
                cnt -= 1
                break
            if left == 3:
                break
        point += len(hit_history) - cnt

    if point > max_point:
        max_point = point
print(max_point)
