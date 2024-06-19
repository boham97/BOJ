from collections import deque

delta = [[-1, 1, 0, 0], [0,0,1,-1]]
def tornedo(l):
    for i in range(0, 2**n, 2**l):
        for j in range(0, 2**n, 2**l):

            temp = [[arr[i + h][j + k] for k in range(2**l)] for h in range(2**l)]
            for k in range(2**l):
                for h in range(2**l):
                    arr[i + h][j - k + 2**l - 1] = temp[k][h]

    melting = [[0] * 2**n for _ in range(2**n)]
    for i in range(2**n):
        for j in range(2**n):
            ice = 0
            for k in range(4):
                di, dj = i + delta[0][k], j + delta[1][k]
                if 0 <= di < 2**n and 0 <= dj < 2**n and arr[di][dj]:
                    ice += 1
            if ice < 3 and arr[i][j]:
                melting[i][j] = 1
    for i in range(2**n):
        for j in range(2**n):
            if melting[i][j]:
                arr[i][j] -= 1

def countIce():
    ice = [0]
    visit = [[0] * 2**n for _ in range(2**n)]
    for i in range(2**n):
        for j in range(2**n):
            if arr[i][j] and not visit[i][j]:
                que = deque()
                que.append((i,j))
                visit[i][j] = 1
                cnt = 0
                while que:
                    x, y = que.popleft()
                    cnt += 1
                    for k in range(4):
                        di, dj = x + delta[0][k], y + delta[1][k]
                        if 0 <= di < 2**n and 0 <= dj < 2**n and arr[di][dj] and not visit[di][dj]:
                            que.append((di, dj))
                            visit[di][dj] = 1
                ice.append(cnt)
    return max(ice)
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**n)]
magic = list(map(int, input().split()))
for i in magic:
    tornedo(i)

print(sum(arr[i][j] for i in range(2**n) for j in range(2**n)))
print(countIce())
