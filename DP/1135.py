def dfs(x):
    for i in son[x]:
        deep[i] = deep[x] + 1
        dfs(i)


n = int(input())
parent = list(map(int, input().split()))
son = [[] for _ in range(n)]
dp = [0] * n
deep = [0] * n

for i in range(1, n):
    son[parent[i]].append(i)

dfs(0)

state = max(deep)
for i in range(state, -1, -1):
    for j in range(n):
        if deep[j] == i:
            if len(son[j]) == 0:
                dp[j] = 1
            else:
                my_son = []
                for s in son[j]:
                    my_son.append(dp[s])
                my_son.sort(reverse = True)
                biggest = 0
                for k in range(len(my_son)):
                    if biggest < my_son[k] + k:
                    biggest = my_son[k] + k
                dp[j] = biggest + 1

print(dp[0] - 1)
