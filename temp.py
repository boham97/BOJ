def f(p):
    if p and p<27:
        print(chr(p+64),end='')
        f(tree[p][0])
        f(tree[p][1])


def m(p):
    if p and p<27:
        m(tree[p][0])
        print(chr(p+64),end='')
        m(tree[p][1])


def e(p):
    if p and p<27:
        e(tree[p][0])
        e(tree[p][1])
        print(chr(p+64),end='')

N = int(input())
tree = [[0,0] for _ in range(27)]
for i in range(N):
    starting, son1, son2 = input().split()
    if son1 != '.':
        tree[ord(starting)-64][0] = ord(son1)-64
        print(ord(starting)-64, ord(son1)-64)
    if son2 != '.':
        tree[ord(starting)-64][1] = ord(son2)-64


f(1)
print()
m(1)
print()
e(1)