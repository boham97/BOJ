from collections import deque

F, S, G, U, D = map(int, input().split()) #F:전체 층수, S현재 층 G목표층U위로 올라가는 층 D내려가는층
visited = [0] *(F+1)
visited[S] = 1
que = deque()
que.append(S)
flag = 0    #목표층 도달 여부
while que:
    now = que.popleft() #현재 위치
    if now == G:
        flag = 1 #도달
    if now + U <= F and visited[now+U] == 0:
        visited[now+U] = visited[now]+1
        que.append(now+U)
    if now - D > 0 and visited[now-D] == 0:
        visited[now-D] = visited[now]+1
        que.append(now-D)

if flag:
    print(visited[G]-1)
else:
    print('use the stairs')