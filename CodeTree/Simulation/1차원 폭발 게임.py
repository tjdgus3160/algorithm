n,m=map(int,input().split())
arr=[int(input()) for _ in range(n)]

while arr:
    flag=False
    cur=arr[0]
    idx=0
    cnt=1
    tmp=[]
    for i in range(1,len(arr)):
        if arr[i]==cur:
            cnt+=1
        else:
            if cnt>=m:
                tmp.append((idx,i-1))
                flag=True
            cur=arr[i]
            idx=i
            cnt=1
    if cnt >= m:
        tmp.append((idx,len(arr)))
        flag = True
    arr2=[]
    prev=0
    for s,e in tmp:
        arr2+=arr[prev:s]
        prev=e+1
    arr2+=arr[prev:]
    arr=arr2
    if not flag:
        break
print(len(arr))
for i in arr:
    print(i)