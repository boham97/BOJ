import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def make_left(a, b, c, d):
    if b < a or d < c:
        return
    root = inorder[b + 1]
    son = post[d]
    print(son, end = ' ')
    #print(a, b, c, d, root, son, 'l')
    i = node[son]
    make_left(a, i -1, c, c -a + i - 1)
    make_right(i+1, b, d - b + i, d - 1)
            

def make_right(a, b, c, d):
    if b < a or d < c:
        return
    root = inorder[a - 1]
    son = post[d]
    print(son, end = ' ')
    #print(a,b, c,d, root, son, 'r')
    i = node[son]
    make_left(a, i -1, c, c -a + i - 1)
    make_right(i+1, b, d - b + i, d - 1)



n = int(input())
inorder = list(map(int, input().split()))
post = list(map(int, input().split()))
node = [0] * (n + 1)
for i in range(n):
    node[inorder[i]] = i
#ans = []
#root node와 좌우 서브트리 찾기
root = post[-1]
target = 0
for i in range(n):
    if inorder[i] == root:
        print(root, end = ' ')
        make_left(0, i -1, 0, i - 1)
        make_right(i + 1, n - 1, i, n -2)
        break