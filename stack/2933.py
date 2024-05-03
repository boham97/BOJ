import sys
input = sys.stdin.readline

delta = [-1, 1, 0, 0]
def printArr():
    for i in range(r):
        for j in range(c):
            print(arr[i][j], end = '')
        print()

def check():
    visit = [[0] * c for _ in range(r + 1)]
    color = 1
    for i in range(r-1, -1, -1):
        for j in range(c):
            if arr[i][j] == '.' or visit[i][j] != 0:
                continue
            stack = [(i,j)]
            visit[i][j] = color
            while stack:
                x, y = stack.pop()
                for k in range(4):
                    dx, dy = x + delta[k], y + delta[3 - k]
                    if 0 <= dx < r + 1 and 0 <= dy < c and arr[dx][dy] == 'x' and visit[dx][dy] == 0:
                        visit[dx][dy] = color                   
                        stack.append((dx, dy))
            color += 1

    if color == 1:
        return
    
    high = r
    for i in range(c):
        bottom = r
        for j in range(r-1, -1, -1):
            if visit[j][i] == 1:
                bottom = j
            elif visit[j][i] == 2:
                high = min(high, bottom - j - 1)
                break
            
    for i in range(c):
        for j in range(r-1, -1, -1):
            if visit[j][i] == 2:
                arr[j + high][i] = 'x'
                arr[j][i] = '.'
    
    
def smash(i):
    floor = r - stick[i]
    logic = False
    if i%2 == 0:
        #left
        for j in range(c):
            if arr[floor][j] == 'x':
                arr[floor][j] = '.'
                logic = True
                break
    else:
        #right
        for j in range(c-1, -1, -1):
            if arr[floor][j] == 'x':
                arr[floor][j] = '.'
                logic = True
                break
    return logic
r, c = map(int, input().split())

arr = list( list(input().rstrip()) for _ in range(r))
arr.append(['x'] * c)
n = int(input())
stick = list(map(int, input().split()))
for i in range(n):
    logic = smash(i)
    #no break -> no check
    if logic: check()
    
printArr()
