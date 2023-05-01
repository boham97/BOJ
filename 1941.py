from collections import deque
ans = 0
arr = [input() for _ in range(5)]
delx = (-1, 1, 0, 0)
dely = (0, 0, 1, -1)
for a in range(19):
    for b in range(a+1, 20):
        for c in range(b+1, 21):
            for d in range(c+1, 22):
                for e in range(d+1, 23):
                    for f in range(e+1, 24):
                        for g in range(f+1, 25):
                            vis = [[0] * 5 for _ in range(5)]
                            que = deque()
                            nums = set([a,b,c,d,e,f,g])
                            que.append((a//5, a%5))
                            score = 0
                            turn = 0
                            s = []
                            vis[a//5][a%5] = 1
                            while turn < 7 and que:
                                x, y = que.popleft()
                                if arr[x][y] == 'S':
                                    score += 1
                                    s.append(5*x+y)
                                turn += 1
                                for k in range(4):
                                    dx, dy = x + delx[k], y+dely[k]
                                    if 0 <= dx < 5 and 0 <= dy < 5:
                                        if dx*5+dy in nums and vis[dx][dy] == 0:
                                            que.append((dx, dy))
                                            vis[dx][dy] = 1
                                
                            if score > 3 and turn == 7:
                                ans += 1

    

print(ans)
