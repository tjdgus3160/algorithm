import sys
input=sys.stdin.readline

n=int(input())
dq=[0]*21
for i in range(n+1):
    if i<4:
        dq[i]=i
    else:
        dq[i]=dq[i-1]+dq[i-2]
print(dq[n])
