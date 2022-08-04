from cmath import inf
import itertools

area = int(input())
population = list(map(int,input().split()))
connecting = [[] for i in range(area)]
for i in range(area):
    connecting[i] = list(map(int,input().split()))
    connecting[i].pop(0)
minpop = inf
min_area =[]
for i in range(1,area//2 + 1):
    for areaA in itertools.combinations(range(1,area+1), i):
        team_A = set()
        last_team_A = set()
        team_A.add(areaA[0])
        while (last_team_A != team_A):
            last_team_A = set(team_A)
            for j in list(team_A):
                for k in areaA:
                    if k in connecting[j-1]:
                        team_A.add(k)            

        areaB = list(set(range(1,area+1))-set(areaA))
        team_B =set()
        last_team_B = set()
        team_B.add(areaB[0])
        while (last_team_B != team_B):
            last_team_B = set(team_B)
            for j in list(team_B):
                for k in areaB:
                    if k in connecting[j-1]:
                        team_B.add(k)

        if set(team_A) == set(areaA) and set(team_B) == set(areaB):
            total_A = 0
            total_B = 0
            for k in areaA:
                total_A += population[k - 1]
            total_B = sum(population) - total_A
            #print(abs(total_A - total_B), areaA)
            if abs(total_A - total_B) < minpop:
                minpop = abs(total_A - total_B)
                min_area = areaA
if minpop == inf:
    print(-1)
else:
 print(minpop)