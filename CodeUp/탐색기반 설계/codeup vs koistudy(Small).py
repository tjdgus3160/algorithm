import sys
input=sys.stdin.readline

n=int(input())
codeup=[*map(int,input().split())]
koisut=[*map(int,input().split())]
res=0
ac=0
bc=0
tmpa=[1000,0]
tmpb=[0,1000]
for i in range(n):
    a,b=codeup[i],koisut[i]
    if a>b:
        res+=a
        ac+=1
        if (tmpa[0]-tmpa[1])>a-b:
            tmpa=[a,b]
    elif a<b:
        res+=b
        bc+=1
        if (tmpb[1]-tmpb[0])>b-a:
            tmpb=[a,b]
    else:
        tmpa=[a,b]
        tmpb=[a,b]
        if ac>bc:
            bc+=1
        else:
            ac+=1
        res+=a
if ac==0:
    res-=tmpb[1]
    res+=tmpb[0]
elif bc==0:
    res-=tmpa[0]
    res+=tmpa[1]
print(res)

