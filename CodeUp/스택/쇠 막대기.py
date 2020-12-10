import sys
input=sys.stdin.readline

tmp=list(input())
l=[]
cnt=0
flag=0
if tmp[-1]=="\n":
    del tmp[-1]
for i in tmp:
    if i=="(":
        l.append(i)
        flag=1
    else:
        l.pop()
        if flag==1:
            cnt+=len(l)
        else:
            cnt+=1
        flag=0
print(cnt)
