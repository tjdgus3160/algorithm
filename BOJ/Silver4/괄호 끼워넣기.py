# 11899번
import sys
input=sys.stdin.readline

s=input().rstrip('\n')
tmp=[]
for i in s:
    if i==')':
        if tmp and tmp[-1]=='(':
            tmp.pop()
        else:
            tmp.append(i)
    else:
        tmp.append(i)
print(len(tmp))