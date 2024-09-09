class Node():
    def __init__(self, key:int, left= None, right =None):
        self.key = key
        self.left = left
        self.right = right


def make_left(a, b, c, d):
    if b < a or d < c:
        return
    root = inorder[b + 1]
    son = post[d]
    pather[son] = root
    print(a, b, c, d, root, son, 'l')
    for i in range(a, b + 1):
        if inorder[i] == son:
            make_right(i+1, b, d - b + i, d - 1)
            

def make_right(a, b, c, d):
    if b < a or d < c:
        return
    root = inorder[a - 1]
    son = post[d]
    pather[son] = root
    print(a,b, c,d, root, son, 'r')
    for i in range(a, b + 1):
        if inorder[i] == son:
            make_right(i+1, b, d - b + i, d - 1)
            make_left(a, i -1, a - 1, i - 2)

n = int(input())
inorder = list(map(int, input().split()))
post = list(map(int, input().split()))
pather = [0] * (n + 1)
#root node와 좌우 서브트리 찾기
root = post[-1]
target = 0
for i in range(n):
    if inorder[i] == root:
        print(i)
        make_right(i + 1, n - 1, i, n -2)
        make_left(0, i -1, 0, i - 1)
        break

print(*pather)