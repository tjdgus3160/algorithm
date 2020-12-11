# 1755번
import sys
input=sys.stdin.readline()

m,n=map(int,input.split())
eng=['zero','one','two','three','four','five','six','seven','eight','nine']
res=[]
for i in range(m,n+1):
    s=""
    if i>=10:
        s+=eng[i//10]
    s+=eng[i%10]
    res.append((s,i))
res.sort(key=lambda x:x[0])
for idx,v in enumerate(res):
    if idx>=10 and idx%10==0:
        print()
    print(v[1],end=' ')