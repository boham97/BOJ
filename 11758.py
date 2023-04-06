import math

p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))


line1 = (p1[0]-p2[0], p1[1]- p2[1])
line2 = (p3[0]-p1[0], p3[1]- p1[1])

temp = line1[0] *line2[1] - line1[1]*line2[0]
if temp >0:
    print(-1)
elif temp <0:
    print(1)
else:
    print(0)
