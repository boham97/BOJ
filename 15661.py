import itertools
import sys
N = int(input())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 1100
for k in range(1,N//2):
    arr = list(itertools.combinations(range(0,N),k))
    for start in arr:
        if ans == 0:
            break
        link = list(set(range(N))-set(start))
        ability = 0
        for j in start:
            for k in start:
                ability += matrix[j][k]
        for j in link:
            for k in link:
                ability -= matrix[j][k]
        diff = abs(ability)
        if diff < ans:
            ans = diff
        #print(ans, start)
print(ans)