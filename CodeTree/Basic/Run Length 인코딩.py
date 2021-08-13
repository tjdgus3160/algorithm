s=input().rstrip()
cur,cnt=None,1
res=""
for i in s:
    if not cur:
        cur=i
    elif i==cur:
        cnt+=1
    else:
        res+=cur+str(cnt)
        cur=i
        cnt=1
res+=cur+str(cnt)
print(len(res))
print(res)