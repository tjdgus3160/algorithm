dp=['0','1','11','12','1121','122111']
n=int(input())
for i in range(6,n+1):
    cur,cnt=None,None
    tmp=''
    for j in dp[-1]:
        if not cur:
            cur=j
            cnt=1
        elif cur==j:
            cnt+=1
        else:
            tmp+=str(cur)+str(cnt)
            cur=j
            cnt=1
    tmp += str(cur) + str(cnt)
    dp.append(tmp)
print(dp[n])