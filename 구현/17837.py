from collections import deque

class mal:
    def __init__(self, x, y, dir):
        self.x = x - 1
        self.y = y - 1
        self.dir = dir - 1
        self.index = 0
    
    def move(self, chess, arr, recur):
        move_flag = False
        d = [(0,1),(0, -1), (-1, 0), (1, 0)]
        x, y = self.x, self.y
        nx, ny = x + d[self.dir][0], y + d[self.dir][1] 

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 2:
            if arr[nx][ny]:
                temp = deque()
                flag = True
                while chess[x][y]:
                    mal = chess[x][y].pop()
                    mal.x = nx
                    mal.y = ny
                    chess[nx][ny].append(mal)
                    #print(mal.index, x, y, nx ,ny, mal.dir)
                    if self == mal:
                        break
            else:
                temp = deque()
                flag = True
                while chess[x][y]:
                    mal = chess[x][y].popleft()
                    if self == mal:
                        flag = False
                    if flag:
                        temp.append(mal)
                    else:
                        mal.x = nx
                        mal.y = ny
                        chess[nx][ny].append(mal)
                        #print(mal.index, x, y, nx ,ny, mal.dir)
                
                chess[x][y] = temp
            
            return True
        else:
            if not recur:
                self.dir += 1 if self.dir % 2 == 0 else -1
                return self.move(chess, arr, 1)
            return False



    


n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
chess = [[deque() for _ in range(n)] for _ in range(n)]
mal_list = [mal(*map(int, input().split())) for _ in range(k)]
i = 1
for m in mal_list:
    chess[m.x][m.y].append(m)
    m.index = i
    i += 1

#print()
ans = False
for i in range(1000):
    for j in range(k):
        m = mal_list[j]
        ans +=m.move(chess, arr, 0)
        #print(m.x, m.y, m.dir)
        if len(chess[m.x][m.y]) > 3:
            print(i + 1)
            exit()
    if not ans:
        print(i + 1)
        exit()
    #print()
else:
    print(-1)