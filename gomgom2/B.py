
N = int(input())
people = []
ans = {'ChongChong'}
for i in range(N):
    a,b = input().split()
    if a not in people:
        people.append(a)
    if b not in people:
        people.append(b)
    if a in ans or b in ans:
        ans.add(a)
        ans.add(b)
print(len(ans))