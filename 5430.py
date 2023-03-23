import sys
from collections import deque

input = sys.stdin.readline


T = int(input())
tc = 0

while (tc < T):
    p = input()
    n = int(input())
    temp = input()
    arr = list(temp[1:-2].split(","))
    logic = 1
    srt = 0
    end = n
    for i in p:
        if i == "D":
            if logic > 0:
                srt += 1
            else:
                end -= 1
        if i == "R":
            logic *= -1

    if(srt > end):
        print("error")
    elif logic < 0:
        print("[",end="")
        print(','.join(arr[srt:end][::-1]),end ="")
        print("]")
    else:
        print("[",end="")
        print(','.join(arr[srt:end]),end="")
        print("]")
    tc += 1
    
