import sys
sys.setrecursionlimit(10**5)

def first_order(num,i):
    if i:
        if son[0][num] < son[0][i]:
            if son[2][num] == 0:
                son[2][num] = i
            else:
                first_order(son[2][num],i)
        if son[0][num] > son[0][i]:
            if son[1][num] == 0:
                son[1][num] = i
            else:
                first_order(son[1][num],i)


def last_order(i):
    if i:
        last_order(son[1][i])
        last_order(son[2][i])
        
        print(son[0][i])
    else:
        return


son = [[0] * 10001 for _ in range(4)] # 값, 자식0,자식1
son[0][0] = 10**6 +1
i = 1
while 1:
    try:
        son[0][i] = int(input())
        first_order(0,i)
        i += 1
    except:
        break
last_order(1)