from sys import stdin
from collections import deque
from itertools import combinations

input = stdin.readline


def bfs():
    global final_ans
    delta = [-1, 1, 0, 0]    
    for g_r_list in combinations(land,g + r):
        for g_list in combinations(g_r_list, g):
            ans = 0
            visit2 = [[0] * M for _ in range(N)]
            que = deque()
            for x, y in g_list:
                que.append((x, y, 1))
                visit2[x][y] = 1
            for x, y in g_r_list:
                if visit2[x][y]:  continue
                que.append((x, y, 2))
                visit2[x][y] = 2
                
            while que:
                x, y, z = que.popleft()
                if z == 1:
                    for i in range(4):
                        dx, dy = x+ delta[i], y + delta[3 - i]
                        if 0 <= dx < N and 0 <= dy < M and arr[dx][dy] != 0 and visit2[dx][dy] ==0:
                            for j in range(4):
                                ddx, ddy = dx+ delta[j], dy + delta[3 - j]
                                if 0 <= ddx < N and 0 <= ddy < M and arr[ddx][ddy] != 0 and visit2[ddx][ddy] == 2:
                                    ans += 1
                                    visit2[dx][dy] = 3
                                    break
                            else:
                                visit2[dx][dy] = 1
                                que.append((dx,dy, 1))
                if z == 2:
                    for i in range(4):
                        dx, dy = x+ delta[i], y + delta[3 - i]
                        if 0 <= dx < N and 0 <= dy < M and arr[dx][dy] != 0 and visit2[dx][dy] ==0:
                                    visit2[dx][dy] = 2
                                    que.append((dx,dy, 2))        
            if ans > final_ans: final_ans = ans
    


final_ans = 0
N, M, g, r = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))
land = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            land.append((i, j))
bfs()

print(final_ans)
