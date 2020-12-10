import sys
input=sys.stdin.readline

cnt=0
res=0
for i in range(5):
    a,b=map(float,input().split())
    t=(b-a-1)
    if t>0:
        if t<4:
            cnt+=t
        else:
            cnt+=4

if cnt<=5:
    res=cnt/0.5*5000*1.05
elif cnt>=15:
    res=cnt/0.5*5000*0.95
else:
    res = cnt / 0.5 * 5000
print(int(res))
