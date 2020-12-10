import sys
input=sys.stdin.readline

tmp=[]
for i in range(9):
    tmp.append([*map(int,input().split())])

a=0
b=0
k=0
for i,v in enumerate(tmp):
    if max(v)>k:
        k=max(v)
        a=i+1
        b=v.index(max(v))+1
print(k)
print(a,b)
