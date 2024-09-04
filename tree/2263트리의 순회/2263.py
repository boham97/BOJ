class Node():
    def __init__(self, key:int, left= None, right =None):
        self.key = key
        self.left = left
        self.right = right

        
n = int(input())
iorder = list(map(int, input().split()))
porder = list(map(int, input().split()))
