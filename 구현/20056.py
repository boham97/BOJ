from collections import deque
def printAns():
    ans = 0
    for i in range(n):
        for j in range(n):
            for m, s, d, t in arr[i][j]:
                ans += m
    print(ans)
    
def go():
    for i in range(n):
        for j in range(n):
            for k in range(len(arr[i][j])):
                if arr[i][j][0][3] != time:
                    break
                m, s, d, t = arr[i][j].popleft()
                di, dj = (i + move[0][d] * s + n)%n, (j + move[1][d] * s + n)%n
                arr[di][dj].append((m, s, d, t + 1))

def devide():
    for i in range(n):
        for j in range(n):
            cnt = 0
            for k in range(len(arr[i][j])):
                if arr[i][j][k][3] == time + 1:
                    cnt += 1
            if cnt < 2:
                continue
            odd, even = False, False
            mass = 0
            velocity = 0
            while arr[i][j] and arr[i][j][0][3] == time + 1:
                m, s, d, t = arr[i][j].popleft()

                mass += m
                velocity += s
                if d%2:
                    even = True
                else:
                    odd = True
                    
            if mass < 5:
                continue
            m = mass//5
            s = velocity//cnt
            if odd != even:
                for k in range(0, 8, 2):
                    arr[i][j].append((m, s, k, t))
            else:
                for k in range(1, 9, 2):
                    arr[i][j].append((m, s, k, t))


n, m, k = map(int, input().split())
move = [[-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]]
arr = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    arr[r - 1][c - 1].append((m, s, d, 0))

for time in range(k):
    go()
    devide()
    

printAns()
