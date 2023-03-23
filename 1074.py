N, r, c = map(int, input().split())

s = [0, 0]
e = [2 ** N - 1, 2**N -1 ]
ans = 0

while (True):
    m = [(s[0] + e[0] + 1)//2, (s[1] + e[1] + 1)//2]
    if r >= m[0] and c >= m[1]:
        ans += 3 * (m[0] - s[0]) ** 2
        s = [m[0], m[1]]
    elif r>= m[0] and c < m[1]:
        ans += 2 * (-s[0] + m[0]) ** 2
        s = [m[0], s[1]]
        e = [e[0], m[1]]
    elif r < m[0] and c >= m[1]:
        ans += (-s[0] + m[0]) ** 2
        s = [s[0], m[1]]
        e = [m[0], e[1]]
    else:
        e = [m[0], m[1]]
    if [r, c] == m or [r,c] == s:
        break

print(ans)
