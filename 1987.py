def dfs(x, y, score):
    global ans
    if score > ans:
        ans = score
    for dx,dy in ((x+1, y), (x-1, y), (x, y + 1), (x, y - 1)):
        if 0 <= dx < R and 0 <= dy < C and not temp[ord(arr[dx][dy])-65]:
                temp[ord(arr[dx][dy])-65] = 1
                dfs(dx, dy, score + 1)
                temp[ord(arr[dx][dy])-65] = 0


if __name__ == "__main__":     
    R, C = map(int, input().split())
    arr = list(input() for _ in range(R))
    ans = 1
    temp = [0 for _ in range(26)]
    temp[ord(arr[0][0])-65] = 1
    
    dfs(0, 0, 1)
    print(ans)