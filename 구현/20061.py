def domino():
    t, x, y = map(int, input().split())
    if t == 1:
        for i in range(6):
            if blue[i][x]:
                blue[i - 1][x] = 1
                break
        else:
            blue[5][x] = 1
            
        for i in range(6):
            if green[i][y]:
                green[i - 1][y] = 1
                break
        else:
            green[5][y] = 1
    elif t == 2:
        for i in range(6):
            if blue[i][x]:
                blue[i - 1][x] = 1
                blue[i - 2][x] = 1
                break
        else:
            blue[5][x] = 1        
            blue[4][x] = 1
            
        for i in range(6):
            if green[i][y] or green[i][y + 1]:
                green[i - 1][y] = 1
                green[i - 1][y + 1] = 1
                break
        else:
            green[5][y] = 1        
            green[5][y + 1] = 1            
    else:
        for i in range(6):
            if blue[i][x] or blue[i][x + 1]:
                blue[i - 1][x] = 1
                blue[i - 1][x + 1] = 1
                break
        else:
            blue[5][x] = 1        
            blue[5][x + 1] = 1
            
        for i in range(6):
            if green[i][y]:
                green[i - 1][y] = 1
                green[i - 2][y] = 1
                break
        else:
            green[5][y] = 1        
            green[4][y] = 1

            
def down(arr, ans):
    for i in range(2,6):
        if sum(arr[i]) == 4:
            arr.pop(i)
            arr.insert(0, ([0] * 4))
            ans += 1
    for i in range(2):
        if sum(arr[i]):
            arr.pop(5)
            arr.insert(0, ([0] * 4))            
        
    
    return ans

def printAll(arr):
    for i in range(6):
        print(arr[i])
    print()
ans = 0
blue = [[0] * 4 for _ in range(6)]
green = [[0] * 4 for _ in range(6)]

for _ in range(int(input())):
    domino()
    ans = down(blue, ans)
    ans = down(green, ans)

print(ans)
print(sum(blue[i][j] + green[i][j] for i in range(6) for j in range(4)))
