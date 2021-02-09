# 12789번
import sys
input=sys.stdin.readline

n=int(input())
arr=[*map(int,input().split())]
tmp=[]
cur=1
flag=True
for i in arr:
    while tmp and tmp[-1]==cur:
        tmp.pop()
        cur+=1
    if i==cur:
        cur+=1
    else:
        if tmp and tmp[-1]<i:
            flag=False
            break
        tmp.append(i)
print('Nice' if flag else 'Sad')