# 19583번
import sys
input=sys.stdin.readline

def calTime(s):
    h,m=map(int,s.split(':'))
    return h*60+m

p=set()
time=[]
res=0
for t in input().rstrip().split(' '):
    time.append(calTime(t))
while True:
    s=input().rstrip()
    if not s:
        break
    t,name=s.split()
    t=calTime(t)
    if t<=time[0]:
        p.add(name)
    elif time[1]<=t<=time[2] and name in p:
        p.remove(name)
        res+=1
print(res)
