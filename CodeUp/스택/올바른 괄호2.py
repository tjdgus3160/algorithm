import sys
input=sys.stdin.readline

tmp=list(input())
l=[]
flag=True
for i in tmp:
    if i=="(":
        l.append(i)
    else:
        if len(l)==0:
            flag=False
            break
        else:
            l.pop()
if flag and len(l)==0:
    print("good")
else:
    print("bad")
