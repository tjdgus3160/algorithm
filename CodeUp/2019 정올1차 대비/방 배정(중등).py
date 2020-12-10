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

group=[m[1]+m[2]+w[1]+w[2],m[3]+m[4],m[5]+m[6],w[3]+w[4],w[5]+w[6]]
res=0
for i in group:
    res+=i//k
    if i%k>0:
        res+=1
print(res)


