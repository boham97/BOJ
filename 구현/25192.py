n = int(input())
input()
ans = 0
i = 1
emo = set()
while i < n:
    i += 1
    name = input()
    if name == "ENTER":
        ans += len(emo)
        emo = set()
        continue
    emo.add(name)
    
ans += len(emo)

print(ans)
