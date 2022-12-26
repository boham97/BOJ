#string = '2+3*4/5'
#string = '(6+5*(2-8)/2)'
string = input()
arr = []
stack =[]
isp = {
    '*': 2,
    '/': 2,
    '+': 1,
     '-': 1,
    '(': 0
}

icp = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 3
}

for i in string:
    if i == '*' or i == '/' or  i == '+' or  i == '-' or  i == '(':
        if stack == []:
            stack.append(i)
        else:
            if isp[stack[-1]] < icp[i]:
                stack.append(i)
            else:
                while isp[stack[-1]] >= icp[i]:
                    arr.append(stack.pop())
                    if len(stack) == 0:
                        break
                stack.append(i)
    elif i != ')':
        arr.append(i)
    else:
        while stack[-1] != '(':
            arr.append(stack.pop())
        stack.pop()
for i in stack[::-1]:
    arr.append(i)
print(''.join(arr))
""" 
    stack2 =[]
    for i in arr:
        if i == '*':
            second, first = stack2.pop(), stack2.pop()
            stack2.append(first * second)
        elif i == '/':
            second, first = stack2.pop(), stack2.pop()
            stack2.append(first / second)
        elif i == '+':
            second, first = stack2.pop(), stack2.pop()
            stack2.append(first + second)
        elif i == '-':
            second, first = stack2.pop(), stack2.pop()
            stack2.append(first - second)
        else:
            stack2.append(i)
    print(f'#{test+1}', *stack2)

 """