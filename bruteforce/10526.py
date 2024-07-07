from itertools import permutations
import time


n, l = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(n))
ans = 0
hap = 2**n -1
my_dict = dict()
st= time.time()
for per in permutations(range(n),  n//2 + 1):
    temp = 0
    cost = 0
    s = per[0]
    for i in per:
        temp += 2**i
        cost += arr[s][i]
        s = i
    key  = str(per[0]) + ' ' + str(per[-1]) + ' ' + str(temp)
    if key not in my_dict:
        my_dict[key] = set()
    my_dict[key].add(cost)

print(my_dict)
for key in my_dict:
    a, b, c = map(int, key.split())
    target = str(b) + ' ' + str(a) + ' ' + str(hap - c)
    print(key, '_', target)
    if target in my_dict:
        print()
et = time.time()
print(et - st)
