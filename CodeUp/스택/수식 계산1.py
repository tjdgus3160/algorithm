import sys
input=sys.stdin.readline

tmp=input().split()
l=[]
for i in tmp:
    if i.isdigit():
        l.append(i)
    else:
        a=l.pop()
        b=l.pop()
        l.append(eval(str(b)+i+str(a)))
print(*l)
