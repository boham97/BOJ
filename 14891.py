gear = [0, 0, 0, 0]
gear_drct = [0, 0, 0, 0]
for i in range(4):
    gear[i] = input()
#print(gear)
order = []
order_logic = 0
orders = int(input())
for i in range(orders):
    order.append(list(map(int, input().split())))
    order[i][0] -= 1
for i in range(orders):
    if order[i][1] == -1:
        gear_drct[order[i][0]] = -1
        order_logic = -1
    else:
        gear_drct[order[i][0]] = 1
        order_logic = 1
    for j in range(order[i][0] + 1, 4):
        if gear[j][6] != gear[j-1][2]:
            gear_drct[j] = order_logic * ((-1) ** (j - order[i][0]))
        else:
            break
    for j in range(order[i][0] - 1, -1, -1):
        if gear[j][2] != gear[j + 1][6]:
            gear_drct[j] = order_logic * ((-1) ** (order[i][0] - j))
        else:
            break
    for j in range(4):
        if gear_drct[j] == 1:
            gear[j] = gear[j][7] + gear[j][0:7]
        elif gear_drct[j] == -1:
            gear[j] = gear[j][1:8] + gear[j][0]
    #print(gear, gear_drct)
    gear_drct = [0, 0, 0, 0]
ans = int(gear[0][0]) + 2 * int(gear[1][0]) + 4 * int(gear[2][0]) + 8 * int(gear[3][0])

print(ans)