n=int(input())
arr=[*map(int,input().split())]
res=[]
end=n+1
while True:
    idx=arr.index(max(arr[:end]))
    res.append(idx+1)
    end=idx
    if idx==0:
        break
print(*res)