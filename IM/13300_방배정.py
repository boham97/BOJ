N, K = map(int,input().split())
arr = [[0,0] for _ in range(7)]
room = 0
for i in range(N):
    sung, grade = map(int,input().split())
    arr[grade][sung] += 1

for i in range(7):
    for j in range(2):
        room += arr[i][j] // K
        if arr[i][j] % K:
            room += 1

print(room)