# 3107번
import sys
input=sys.stdin.readline

arr=input().rstrip().split(':')
res=[]
for i in arr:
    res.append(('0'*4+i)[-4:])
if len(res)<8:
    idx=res.index('0000')
    for _ in range(8-len(res)):
        res.insert(idx,'0000')
elif len(res)>8:
    while len(res)!=8:
        res.remove('0000')
print(':'.join(res))
