# 후위표기법
priority = {'*':3,'/':3,'+':2,'-':2,'(':1}
expr=[]
operator = []
result=[]
tmp=input('식을 입력하세요: ')

#공백 제거
for i in tmp:
    if i ==' ':
        continue
    expr.append(i)

for i in expr:
    if i == '(':
        operator.append(i)
    elif i in '+-*/':
        if len(operator)==0:
            operator.append(i)
        else:
            if priority[operator[-1]] >= priority[i]:
                result.append(operator.pop())
                operator.append(i)
            else:
                operator.append(i)
    elif i == ')':
        while True:
            tmp = operator.pop()
            if tmp == '(':
                break
            result.append(tmp)

    else:
        result.append(i)

while len(operator)!=0:
    result.append(operator.pop())

print(''.join(result))