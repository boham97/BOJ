class Node():
    def __init__(self, key:int, left= None, right =None):
        self.key = key
        self.left = left
        self.right = right


def make_left(left: int, right: int, post_root: int):
    root = post[post_root]
    if right < left:
        return
    left_son = post[right]
    print(left, right, root, left_son, "left")
    pather[left_son] = root
    for i in range(left, right + 1):
        if inorder[i] == left_son:
            make_left(left, i - 1, left_son)
            make_right(i + 1, right, left_son)
            break

def make_right(left: int, right: int, post_root: int):
    if right < left:
        return
    right_son = post[right - 1]
    print(left, right, root, right_son, "right")
    pather[right_son] = root
    for i in range(left, right + 1):
        if inorder[i] == right_son:
            make_left(left, i - 1, right_son)
            make_right(i + 1, right, right_son)
            break    


n = int(input())
inorder = list(map(int, input().split()))
post = list(map(int, input().split()))
pather = [0] * (n + 1)
#root node와 좌우 서브트리 찾기
root = post[-1]
target = 0
for i in range(n):
    if inorder[i] == root:
        target = i
        make_left(0, i - 1, n - 1)
        make_right(i + 1, n - 1, n - 1)
        break

print(*pather)