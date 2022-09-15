import itertools
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
#한팀에 최대 10명 차이는 최대 1000
ans = 1100
#combinations으로 정한 팀을 모두 찾을 필요없다
arr = list(itertools.combinations(range(0,N),N//2))
for i in range(len(arr)//2):
    #차이가 0이면 탐색중단
    if ans == 0:
        break
    start = arr[i]
    link = arr[len(arr)-i-1]
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