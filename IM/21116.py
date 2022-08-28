cases = int(input())
arr = [list(map(int,input().split())) for _ in range(cases)]
dict  ={
    '0': 5,
    '1': 3,
    '2': 4,
    '5': 0,
    '3': 1,
    '4': 2,
}
max_ans = 0
for i in range(6):
    ans = 0
    top = arr[0][dict[str(i)]]
    for j in range(cases):
        bottom = top
        top = arr[j][dict[str(arr[j].index(bottom))]]
        ans += max({1,2,3,4,5,6} - {bottom, top})
    if ans > max_ans:
        max_ans = ans
print(max_ans)