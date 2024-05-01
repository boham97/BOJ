class Trie():
    def __init__(self):
        self.head = Node()

    def insert(self, arr):
        now = self.head
        for i in range(1, len(arr)):
            key = arr[i]
            if key not in now.child:
                now.child[key] = Node(key)
            now = now.child[key]
                
class Node():
    def __init__(self, data = None):
        self.end = False
        self.child = {}
        self.data = data
    def dfs(self, floor):
        if self.data:
            print("--"*(floor - 1) + self.data)
        self.child = dict(sorted(self.child.items()))
        for c in self.child:
            self.child[c].dfs(floor + 1)
n = int(input())
trie =Trie()
for _ in range(n):
    arr = list(input().split())
    trie.insert(arr)
trie.head.dfs(0)
    
