ans = [0] * 100
ans[0], ans[1], ans [2] = 1,1,1

for i in range(3,100):
    ans[i] = ans[i-3] + ans[i-2]

tc = int(input())
for test in range(tc):
    case = int(input())
    print(ans[case-1])
