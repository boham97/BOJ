long = int(input())
oper = long // 2
sentence = list(input())
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
if long >= 3:
    operator_condition = [0 for i in range(oper)]
else:
    operator_condition =[2] 
while(operator_condition[0]<2):
    logic = 0
    for i in range(len(operator_condition)-1,0,-1):
        if operator_condition[i] >= 2:
            operator_condition[i] -= 2
            operator_condition[i-1] += 1
    for i in range(len(operator_condition)-1):
            if operator_condition[i] + operator_condition[i+1] == 2:
                operator_condition[i + 1] = 0
                operator_condition[i] += 1
                if operator_condition[i] == 2:
                    logic += 1
    if logic >0:
        continue
    #print(operator_condition)

    result2 = 0
    temp = sentence[:]
    oper_con = operator_condition[:]
    while(sum(oper_con) >= 1):
        pos = oper_con.index(1)
        if temp[2 * pos + 1] == '+':
            temp[2*pos + 1] = str(int(temp[2*pos])+int(temp[2*pos+2]))
            temp.pop(2*pos+2)
            temp.pop(2*pos )
            oper_con.pop(pos)
        elif temp[2*pos+1] == '-':
            temp[2*pos + 1] = str(int(temp[2*pos])-int(temp[2*pos+2]))
            temp.pop(2*pos+2)
            temp.pop(2*pos)
            oper_con.pop(pos)
        elif temp[2*pos+1] == '*':
            temp[2*pos + 1] = str(int(temp[2*pos])*int(temp[2*pos+2]))
            temp.pop(2*pos+2)
            temp.pop(2*pos)
            oper_con.pop(pos)
    
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
    #print(operator_condition)
    #print(temp, result2)
    operator_condition[len(operator_condition)-1] += 1 
    
print(result)
