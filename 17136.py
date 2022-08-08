import itertools

input_arr = [list(map(int,input().split())) for _ in range(10)]
cnt = 0
for i in range(10):
    cnt += input_arr[i].count(1)

print(cnt)

min_paper = 25

test_arr = [[] for _ in range(10)]

while(1):
    pass