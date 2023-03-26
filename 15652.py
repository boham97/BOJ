from itertools import permutations

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
ans_set = set()

for ans in permutations(arr, M):
    if str(ans) not in ans_set:
        print(*ans)
        ans_set.add(str(ans))