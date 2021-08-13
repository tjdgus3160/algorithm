n=int(input())
arr=[*map(int,input().split())]
res=0
k=None
for i in arr:
    if not k or i<k:
        k=i
    elif i>k:
        res=max(res,i-k)
print(res)