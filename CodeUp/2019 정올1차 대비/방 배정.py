import sys
input=sys.stdin.readline

n,k=map(int,input().split())
m=[0,0,0,0,0,0,0]
w=[0,0,0,0,0,0,0]
for i in range(n):
    a, b = map(int, input().split())
    if a==1:
        m[b]+=1
    else:
        w[b]+=1

res=0
for i in range(1,7):
    res+=m[i]//k
    if m[i]%k>0:
        res+=1
    res+=w[i]//k
    if w[i]%k>0:
        res+=1
print(res)

