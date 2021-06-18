# 2852번
import sys
input=sys.stdin.readline

def difftime(before,after):
    if after[1]>=before[1]:
        return [after[0]-before[0],after[1]-before[1]]
    else:
        return [after[0]-before[0]-1,after[1]-before[1]+60]

def addtime(time,tmp):
    time[1]+=tmp[1]
    if time[1]>=60:
        time[0]+=1
        time[1]-=60
    time[0]+=tmp[0]

a,b=0,0
time=[0,0]
t1,t2=[0,0],[0,0]
winer=0
for _ in range(int(input())):
    n,t=input().split()
    tmp=[*map(int,t.split(':'))]
    if n=='1':
        a+=1
        if not winer or a-b==1:
            winer=1
            time[0],time[1]=tmp[0],tmp[1]
        elif winer==2 and a==b:
            diff=difftime(time,tmp)
            addtime(t2,diff)
            winer=0
    else:
        b+=1
        if not winer or b-a==1:
            winer=2
            time[0],time[1]=tmp[0],tmp[1]
        elif winer==1 and a==b:
            diff = difftime(time,tmp)
            addtime(t1, diff)
            winer=0
if a>b:
    diff=difftime(time,[48,0])
    addtime(t1,diff)
elif b>a:
    diff=difftime(time,[48,0])
    addtime(t2,diff)
print('%02d:%02d'%(t1[0],t1[1]))
print('%02d:%02d'%(t2[0],t2[1]))
