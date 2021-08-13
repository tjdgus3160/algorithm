a,b=map(int,input().split())
res=0
for i in range(a,b+1):
    k=1
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            k+=j+(i//j)
            if j==i//j:
                k-=j
    if k==i:
        res+=1
print(res)