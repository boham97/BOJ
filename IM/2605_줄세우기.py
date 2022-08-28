#2605 줄세우기 b2

people = int(input())
soon = list(map(int,input().split()))
arr =[]
for i in range(0,people):
    arr.insert(soon[i],i+1)
print(*arr[::-1])