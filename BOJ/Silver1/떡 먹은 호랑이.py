# 2502번
import sys
input=sys.stdin.readline

d,k=map(int,input().split())
day=[0,0,0,[1,1],[1,2],[2,3]]
for _ in range(6,31):
    day.append([day[-1][0]+day[-2][0],day[-1][1]+day[-2][1]])
a,b=day[d]
aa=a
res=[]
while True:
    if (k-aa)%b==0:
        res=[aa//a,(k-aa)//b]
        break
    aa+=a
for i in res:
    print(i)