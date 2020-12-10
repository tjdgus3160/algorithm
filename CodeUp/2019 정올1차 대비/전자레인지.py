t=int(input())
tmp=t
l=[0,0,0]
if (tmp//300)>0:
    a=tmp//300
    tmp=tmp-a*300
    l[0]=a
if (tmp//60)>0:
    a=tmp//60
    tmp=tmp-a*60
    l[1]=a
if (tmp//10)>0:
    a=tmp//10
    tmp=tmp-a*10
    l[2]=a
if tmp>0:
    print(-1)
else:
    for i in l:
        print(i,end=" ")
