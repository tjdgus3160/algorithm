import sys
input=sys.stdin.readline

tmp=[]
for i in range(int(input())):
    tmp.append(int(input()))
res=[]
for i in tmp:
    if i==0:
        res.pop()
    else:
        res.append(i)
print(sum(res))
