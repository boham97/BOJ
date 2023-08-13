dic =dict()
dic[0] = 1
N, P, Q = map(int, input().split())
def func(now):
    if now in dic.keys():
        return dic[now]
    else:
        temp = func(now//P) + func(now//Q)
        dic[now] = temp
        return temp

print(func(N))
