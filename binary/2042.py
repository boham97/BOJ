def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) //2
    tree[node] = init(start, mid, node *2) + init(mid + 1, end , node *2 + 1)
    return tree[node]


def sum(start, end, node, left, right):
    if left > end or right < start: return 0
    if left <= start and right >= end: return tree[node]
    mid = (start + end) //2
    return sum(start, mid, node *2, left, right) + sum(mid + 1, end, node * 2 + 1, left, right)


def update(start, end, node, target, diff):
    if start > target or end  < target: return
    tree[node] += diff
    if start == end: return
    mid = (start + end) //2
    update(start, mid, node * 2, target, diff)
    update(mid + 1, end, node  * 2 + 1, target, diff)
    

n, m, k = map(int, input().split())
tree = [0] * (4 * n)
arr = [0] * n
for i in range(n):
    arr[i] = int(input())
init(0, n -1, 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, n - 1, 1, b - 1, c - arr[b - 1])
        arr[b - 1] = c
    else:
        print(sum(0, n -1, 1, b - 1, c - 1))

