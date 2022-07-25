long = int(input())
oper = long // 2
sentence = input()
result = 0
for i in range(len(sentence)):
    if i == 0:
        result += int(sentence[i])
    elif i % 2 == 0:
        if sentence[i-1] == '+':
            result += int(sentence[i])
        elif sentence[i-1] == '-':
            result -= int(sentence[i])
        elif sentence[i-1] == '*':
            result = result * int(sentence[i])
#print(result)
operator_condition = [0 for i in range(oper)]
while(operator_condition[0]<2):
    result2 = 0
    temp = sentence
    for i in range(oper):
        if operator_condition[i] == 1:
            if sentence[2*i-1] == '+':
                temp = temp[:2*i-2]+ str(int(sentence[2*i-2])+int(sentence[2*i])) + temp[2*i+1:]
            elif sentence[2*i-1] == '-':
                temp = temp[:2*i-2]+ str(int(sentence[2*i-2])-int(sentence[2*i])) + temp[2*i+1:]
            elif sentence[2*i-1] == '*':
                temp = temp[:2*i-2]+ str(int(sentence[2*i-2])*int(sentence[2*i])) + temp[2*i+1:]
    for i in range(len(temp)):
        if i == 0:
            result2 += int(temp[i])
        elif i % 2 == 0:
            if temp[i-1] == '+':
                result2 += int(temp[i])
            elif temp[i-1] == '-':
                result2 -= int(temp[i])
            elif temp[i-1] == '*':
                result2 = result2 * int(temp[i])
    if result2 > result:
        result = result2
    logic = 0
    while(logic == 0):
        operator_condition[len(operator_condition)-1] += 1
        for i in range(len(operator_condition)-2):
            if operator_condition[i] + operator_condition[i+1] == 2:
                operator_condition[len(operator_condition)-1] += 1
        for i in range(len(operator_condition)-1,0,-1):
            if operator_condition[i] >= 2:
                operator_condition[i] -= 2
                operator_condition[i-1] += 1
    print(operator_condition)
print(result)