




def move(d, s):
  for i in range(len(cloud)):
      cloud[i][0] = (cloud[i][0] + n + delta[0][d] *s)%n
      cloud[i][1] = (cloud[i][1] + n + delta[1][d] *s)%n
def drop():
  for i, j in cloud:
      arr[i][j] += 1
def magic():
  for i,j in cloud:
      water = 0
      for k in range(2, 10, 2):
          di, dj = i + delta[0][k], j + delta[1][k]
          if 0<= di < n and 0 <= dj < n and arr[di][dj]:
              water += 1
      arr[i][j] += water
def create():
    visit = [[1] * n for _ in range(n)]
    for k in range(len(cloud) - 1, -1, -1):
        i, j = cloud[k]
        visit[i][j] = 0
        cloud.pop()

    for i in range(n):
        for j in range(n):
            if arr[i][j] > 1 and visit[i][j]:
                cloud.append([i, j])
                arr[i][j] -= 2

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cloud = [[n - 2, 0], [n - 2, 1], [n - 1, 0],[n - 1, 1]]
delta = [[0,0,-1,-1,-1,0,1,1,1],[0,-1,-1,0,1,1,1,0,-1]]
for _ in range(m):
    d, s = map(int, input().split())
    move(d, s)
    drop()
    magic()
    create()

print(sum(arr[i][j] for i in range(n) for j in range(n)))
