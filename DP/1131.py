a,b, k = map(int, input().split())
arr = [i for i in range(4000001)]
visit = [0] * 4000001
arr[1] = 1
visit[1] = 1
for i in range(1, b+1):
    if visit[i]:  #사이클 탔다면 확인X
        continue
    target = set()
    min_ = i
    num = i
    while visit[num] == 0 and num not in target:  # 대상 찾기 사이클 감지하면 멈
        target.add(num)
        res = 0
        while num:
            j = num %10
            res += j ** k
            num = num // 10
        if res < min_:
            min_ = res
        num = res
    target.add(res)
    arr[i] = min(min_, arr[num])
    num = res
    min_cycle = res
    cycle = []
    while visit[num] == 0:  # cycle도는거만 visit처리
        cycle.append(num)
        visit[res] = 1
        res = 0
        while num:
            j = num %10
            res += j ** k
            num = num // 10
        if res < min_cycle:
            min_cycle = res
        num = res
    for i in cycle:
        arr[i] = min_cycle
        
ans = 0

for k in range(a, b+1):
    ans += arr[k]
print(ans)
