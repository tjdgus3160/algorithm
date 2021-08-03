n=int(input())
arr=[*map(int,input().split())]
a,b=map(int,input().split())
res=0
for i in arr:
    i-=a
    res+=1
    if i>0:
        m,r=i//b,i%b
        res+=m
        if r:
            res+=1
print(res)