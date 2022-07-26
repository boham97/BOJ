"""
같은 코드이나 리스트에 저장하지 않고 변수에 저장후 갱신
72ms
모두 보는 경우가 있는것 같음!
리스트에 저장하는게 더 빠르다?

f, g= 0, 1
N = int(input())
for n in range(1,N):
    g,f = f, f + g
print(f+g)
"""


"""
    모든 경우를 찾은뒤 출력
    f는 끝이 0으로 끝나는 이친수
    g는 1로 끝나는 이친수
    1로 끝나면 다음번에 무조건 0
    0으로 끝나면 1과 0 모두 선택가능
    따라서
    f(n) = f(n-1) + g(n-1)
    g(n) = f(n-1)
    68ms
"""
f = [0] * 90
g = [0] * 90

g[0] = 1

for n in range(1,90):
    f[n] = f[n-1] + g[n-1]
    g[n] = f[n-1]

N = int(input())
N -= 1
print(f[N]+g[N])
