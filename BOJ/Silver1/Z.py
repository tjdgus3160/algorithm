# 1074번
n,r,c=map(int,input().split())
a=bin(r)[2:]
b=bin(c)[2:]
if len(a)>len(b):
    b="0"*(len(a)-len(b))+b
elif len(a)<len(b):
    a="0"*(len(b)-len(a))+a
l=[]
for i in range(len(a)):
    l.append("0b"+a[i]+b[i])
result=0
for i in l:
    result=result*4+int(i,2)
print(result)