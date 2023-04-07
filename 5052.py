class Node():
    def __init__(self):
        self.root = {}

    def insert(self, number):
        node = self.root

        for num in number:
            if "end" in node.keys():
                return False
            if num not in node:
                node[num] = {}
            node = node[num]
        node["end"] = number

        return True

t = int(input())
for test in range(t):
    num = int(input())
    node = Node()
    logic = 1
    arr = []
    for _ in range(num):
        arr.append(input())
    arr.sort()
    for call_number in arr:
        if logic and not node.insert(call_number):
            logic = 0
    if logic:
        print("YES")
    else:
        print("NO")
