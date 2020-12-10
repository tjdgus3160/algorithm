def bi(k):
    s=0
    e=len(ll)-1
    m=len(ll)//2
    while True:
        if ll[m]==k:
            return m
        elif ll[m]<k:
            s=m+1
            m=(s+e)//2
        else:
            e=m-1
            m=(s+e)//2

n=int(input())
l=list(map(int,input().split()))
ll=sorted(l)
result=[0]*n
for i in range(n):
    result[i]=bi(l[i])
for i in result:
    print(i,end=" ")
