from collections import defaultdict

n, q= map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()
dic = defaultdict(int)
for i in range(n):
    dic[arr[i]] = i

for _ in range(q):
    req = int(input())
    print(dic[req] * (n-dic[req] -1))
