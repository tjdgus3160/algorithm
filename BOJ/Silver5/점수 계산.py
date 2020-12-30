# 2822번
import sys
input=sys.stdin.readline

a=[]
for i in range(8):
    a.append((i+1,int(input())))
a.sort(key=lambda x:-x[1])
k=0
res=[]
for _ in range(5):
    i,p=a.pop(0)
    res.append(i)
    k+=p
res.sort()
print(k)
print(*res)