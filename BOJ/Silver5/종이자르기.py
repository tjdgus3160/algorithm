# 2628번
import sys
input=sys.stdin.readline

m,n=map(int,input().split())
x=[0]
y=[0]
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a==0:
        y.append(b)
    else:
        x.append(b)
x.append(m)
y.append(n)
x.sort()
y.sort()
rx=0
for i in range(1,len(x)):
    rx=max(rx,x[i]-x[i-1])
ry=0
for i in range(1,len(y)):
    ry=max(ry,y[i]-y[i-1])
print(rx*ry)