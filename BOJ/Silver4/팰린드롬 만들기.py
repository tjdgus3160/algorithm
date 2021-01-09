# 1213번
import operator
from collections import Counter
import sys
input=sys.stdin.readline

s=list(input().rstrip('\n'))
n=len(s)
tmp=[]
center=""
flag=True
for k,v in sorted(Counter(s).items(),key=operator.itemgetter(0)):
    if v%2==1:
        if center=="":
            center=k
            tmp+=[k]*((v-1)//2)
        else:
            flag=False
            break
    else:
        tmp+=[k]*(v//2)
if flag:
    res=tmp+[center]
    tmp.reverse()
    res+=tmp
    print("".join(res))
else:
    print("I'm Sorry Hansoo")