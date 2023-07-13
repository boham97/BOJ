

class Cube:
    def __init__(self):
        self.id = 0
        self.color = [-1,-1,-1,-1,-1,-1,-1]

arr2 = ['w','g', 'r', 'b', 'o','y','error']


def um(layer):
    temp = [[] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            temp[i].append(arr[layer][i][j])
    for i in range(3):
        for j in range(3):
            arr[layer][i][j] = temp[j][2-i]

    for i in range(3):
        for j in range(3):
            temp_color = arr[layer][i][j].color[1]
            for k in range(4,1,-1):
                arr[layer][i][j].color[k] = arr[layer][i][j].color[k-1]
            arr[layer][i][j].color[1] = arr[layer][i][j].color[6]
            arr[layer][i][j].color[6] = arr[layer][i][j].color[4]
            
def up(layer):
    temp = [[] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            temp[i].append(arr[layer][i][j])
    for i in range(3):
        for j in range(3):
            arr[layer][i][j] = temp[2-j][i]

    for i in range(3):
        for j in range(3):
            temp_color = arr[layer][i][j].color[1]
            for k in range(1,4):
                arr[layer][i][j].color[k] = arr[layer][i][j].color[k+1]
            arr[layer][i][j].color[6] = temp_color
            arr[layer][i][j].color[4] = temp_color


def lm(layer):
    temp = [[] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            temp[i].append(arr[i][j][layer])
    for i in range(3):
        for j in range(3):
            arr[i][j][layer] = temp[j][2-i]

    for i in range(3):
        for j in range(3):
            temp_color = arr[i][j][layer].color[0]
            link = [0,2,5,6]
            for k in range(3):
                arr[i][j][layer].color[link[k]] = arr[i][j][layer].color[link[k+1]]
            arr[i][j][layer].color[6] = temp_color
            arr[i][j][layer].color[4] = temp_color
        

def lp(layer):
    temp = [[] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            temp[i].append(arr[i][j][layer])
    for i in range(3):
        for j in range(3):
            arr[i][j][layer] = temp[2-j][i]

    for i in range(3):
        for j in range(3): 
            temp_color = arr[i][j][layer].color[6]
            link = [6,5,2,0]
            for k in range(3):
                arr[i][j][layer].color[link[k]] = arr[i][j][layer].color[link[k+1]]
            arr[i][j][layer].color[0] = temp_color
            arr[i][j][layer].color[4] = arr[i][j][layer].color[6]

def fm(layer):
    temp = [[] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            temp[i].append(arr[i][layer][j])
    for i in range(3):
        for j in range(3):
            arr[i][layer][j] = temp[j][2-i]

    for i in range(3):
        for j in range(3):
            link = [0,3,5,1]
            temp_color = arr[i][layer][j].color[0]
            for k in range(3):
                arr[i][layer][j].color[link[k]] = arr[i][layer][j].color[link[k+1]]
            arr[i][layer][j].color[1] = temp_color

            
def fp(layer):
    temp = [[] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            temp[i].append(arr[i][layer][j])
    for i in range(3):
        for j in range(3):
            arr[i][layer][j] = temp[2-j][i]

    for i in range(3):
        for j in range(3):
            temp_color = arr[i][layer][j].color[1]
            link = [1,5,3,0]
            for k in range(3):
                arr[i][layer][j].color[link[k]] = arr[i][layer][j].color[link[k+1]]
            arr[i][layer][j].color[0] = temp_color


def ans():
    for i in range(3):
        for j in range(3):
            print(arr2[arr[0][i][j].color[0]], end='')
        print()
        
def id():
    for i in range(3):
        for j in range(3):
            for k in range(3):
                print(arr[i][j][k].color, end=' ')
            print()
        print()

N = int(input())
for _ in range(N):
    arr = [[[Cube() for _ in range(3)] for _ in range(3)] for _ in range(3)]

    #init
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i == 0:
                    arr[i][j][k].color[0] = 0
                if i == 2:
                    arr[i][j][k].color[5] = 5
                if j == 0:
                    arr[i][j][k].color[4] = 4
                    arr[i][j][k].color[6] = 4
                if j == 2:
                    arr[i][j][k].color[2] = 2
                if k == 0:
                    arr[i][j][k].color[1] = 1
                if k == 2:
                    arr[i][j][k].color[3] = 3
                arr[i][j][k].id = 9*i + 3*j + k
    k = int(input())
    orders = list(input().split())
    for order in orders:
        if order[0] == 'F':
            if order[1] == '+':
                fp(2)
            else:
                fm(2)
        if order[0] == 'B':
            if order[1] == '+':
                fm(0)
            else:
                fp(0)
        if order[0] == 'L':
            if order[1] == '+':
                lp(0)
            else:
                lm(0)
        if order[0] == 'U':
            if order[1] == '+':
                up(0)
            else:
                um(0)
        if order[0] == 'D':
            if order[1] == '+':
                um(2)
            else:
                up(2)
        if order[0] == 'R':
            if order[1] == '+':
                lm(2)
            else:
                lp(2)
    
    
    ans()
