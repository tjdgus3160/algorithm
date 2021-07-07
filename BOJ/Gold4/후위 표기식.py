# 1918번
import sys
input=sys.stdin.readline

s=input().rstrip()
dic={'*':3,'/':3,'+':2,'-':2,'(':1}
op=[]
res=[]

for i in s:
    if i =='(':
        op.append(i)
    elif i in '*/+-':
        while op and dic[op[-1]]>=dic[i]:
            res.append(op.pop())
        op.append(i)
    elif i ==')':
        while op and op[-1]!='(':
            res.append(op.pop())
        op.pop()
    else:
        res.append(i)

while op:
    res.append(op.pop())
print(''.join(res))