import sys
input=sys.stdin.readline

a=list(input())
if a[-1]=="\n":
    del a[-1]
res=[]
cnt=0
for i in a:
    if len(res)==0:
        cnt+=10
    elif i!=res[-1]:
        cnt+=10
    elif i==res[-1]:
        cnt+=5
    res.append(i)
print(cnt)
