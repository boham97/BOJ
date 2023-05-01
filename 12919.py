S = input()
T = input()
ans = [0]
def func(t):
    if len(S) == len(t):
        if S == t:
            ans[0] =1
        return
    
    if t[-1] == 'A':
        func(t[:-1])
    if t[0] == 'B':
        func(t[1:][::-1])
    
func(T)
print(ans[0])
