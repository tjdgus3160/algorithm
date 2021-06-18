# 3758번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n,k,t,m=map(int,input().split())
    cnt=[0]*(n+1)
    score=[[0]*(k+1) for _ in range(n+1)]
    time=[0]*(n+1)
    for idx in range(m):
        i,j,s=map(int,input().split())
        cnt[i]+=1
        score[i][j]=max(score[i][j],s)
        time[i]=idx
    res=1
    S=sum(score[t])
    C=cnt[t]
    T=time[t]
    for i in range(1,n+1):
        if i==t:
            continue
        ss=sum(score[i])
        if ss>S:
            res+=1
        elif ss==S:
            cc=cnt[i]
            if cc<C:
                res+=1
            elif cc==C:
                if time[i]<T:
                    res+=1
    print(res)