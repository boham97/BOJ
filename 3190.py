num_mat = int(input())
num_apple = int(input())
mat = [[0 for _ in range(num_mat)] for i in range(num_mat)]
for i in range(num_apple):
    x, y = list(map(int,input().split()))
    mat[x - 1][y - 1] = 1
order_num = int(input())
order = [[],[]]
for i in range(order_num):
    a, b = list(input().split())
    order[0].append(int(a))
    order[1].append(b)
direction = 3
t = 0
snake = [[0, 0]]
while(1):
    #print(t,direction, snake)
    if direction == 0 and snake[0][0] + 1 < num_mat and [snake[0][0] + 1, snake[0][1]] not in snake:
        if  mat[snake[0][0] + 1][snake[0][1]] == 1:
            mat[snake[0][0] + 1][snake[0][1]] = 0
            snake.insert(0,[snake[0][0] + 1, snake[0][1]])
        else:
            snake.insert(0,[snake[0][0] + 1, snake[0][1]])
            snake.pop()

    elif direction == 1 and snake[0][1] - 1 >= 0 and [snake[0][0], snake[0][1] - 1] not in snake:
        if  mat[snake[0][0]][snake[0][1] - 1] == 1:
            mat[snake[0][0]][snake[0][1] - 1] = 0
            snake.insert(0,[snake[0][0], snake[0][1] - 1])
        else:
            snake.insert(0,[snake[0][0], snake[0][1] - 1])
            snake.pop()

    elif direction == 2 and snake[0][0] - 1 >= 0 and [snake[0][0] - 1, snake[0][1]] not in snake:
        if  mat[snake[0][0] - 1][snake[0][1]] == 1:
            mat[snake[0][0] - 1][snake[0][1]] = 0
            snake.insert(0,[snake[0][0] - 1, snake[0][1]])
        else:
            snake.insert(0,[snake[0][0] - 1, snake[0][1]])
            snake.pop()
    
    elif direction == 3 and snake[0][1] + 1 < num_mat and [snake[0][0], snake[0][1] + 1] not in snake:
        if  mat[snake[0][0]][snake[0][1] + 1] == 1:
            mat[snake[0][0]][snake[0][1] + 1] = 0
            snake.insert(0,[snake[0][0], snake[0][1] + 1])
        else:
            snake.insert(0,[snake[0][0], snake[0][1] + 1])
            snake.pop()
    else:
        break
    t += 1
    if t in order[0]:
        temp = order[1][order[0].index(t)]
        if temp == 'L':
            direction -= 1
            if direction == -1:
                direction = 3
        else:
            direction += 1
            if direction == 4:
                direction = 0
    
print(t+1)