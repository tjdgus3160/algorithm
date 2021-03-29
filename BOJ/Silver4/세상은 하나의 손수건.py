# 20493번
import sys
input=sys.stdin.readline

dic={'u':[0,1],'r':[1,0],'d':[0,-1],'l':[-1,0]}
direct=['u','r','d','l']
cur='r'
time=0
res=[0,0]
n,t=map(int,input().split())
if n==0:
    print(t,0)
    exit()
for _ in range(n):
    k,s=input().split()
    res=[res[0]+(int(k)-time)*dic[cur][0],res[1]+(int(k)-time)*dic[cur][1]]
    time=int(k)
    if s=='right':
        cur=direct[(direct.index(cur)+1)%4]
    else:
        cur=direct[(direct.index(cur)-1)%4]
res=[res[0]+(t-time)*dic[cur][0],res[1]+(t-time)*dic[cur][1]]
print(*res)