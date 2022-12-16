# set 사용
""" 
tc = int(input())
for test in range(tc):
    N = int(input())
    note1 = set(list(map(int, input().split())))
    M = int(input())
    note2 = list(map(int, input().split()))
    for i in range(M):
        if note2[i] in note1:
            print(1)
        else:
            print(0)
 """
# binary serach쓰기
from bisect import bisect_left


tc = int(input())
for test in range(tc):
    N = int(input())
    note1 = list(map(int, input().split()))
    note1.sort()
    M = int(input())
    note2 = list(map(int, input().split()))
    for i in range(M):
        index = bisect_left(note1, note2[i])
        if index < N and note1[index] == note2[i]:
            print(1)
        else:
            print(0)