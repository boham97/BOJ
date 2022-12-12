
"""
D (3 ≤ D ≤ 30)
K (10 ≤ K ≤ 100,000)
A, B (1≤ A ≤ B)
"""
import collections
deq = collections.deque([1,0,0,1])
D, K = map(int, input().split())
for i in range(3,D+1):
    temp1, temp2 = deq[0]+deq[2],deq[1]+deq[3]
    deq.popleft()
    deq.popleft()
    deq.append(temp1)
    deq.append(temp2)
a, b = deq[2], deq[3]
for A in range(1,K//a):
    if (K-(A*a))%b == 0:
        break
print(A)
print((K-(A*a))//b)
