a,b=map(int,input().split())
res=0
for i in range(a,b+1):
    if i==1:
        continue
    if int(i**0.5)**2==i:
        for j in range(2,int(i**0.5)):
            if i%j==0:
                break
        else:
            res+=1
print(res)