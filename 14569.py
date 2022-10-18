N = int(input())
lesson = [0] * N
for i in range(N):
    temp = list(map(int,input().split()))
    for j in temp[1:]:
        lesson[i] = lesson[i]|1<<j
M = int(input())
people = [0] * M
for i in range(M):
    temp = list(map(int,input().split()))
    for j in temp[1:]:
        people[i] = people[i]|1<<j

ans = [0] * M
for i in range(M):
    for j in range(N):
        if lesson[j] == lesson[j]&people[i]:
            ans[i]+= 1


for i in ans:
    print(i)
