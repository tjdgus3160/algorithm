# 17413번
import sys
input=sys.stdin.readline

s=input().rstrip('\n')
res=[]
tmp=[]
for i in s:
    if not tmp:
        tmp.append(i)
        continue
    if tmp[0]=='<':
        if i == '>':
            tmp.append(i)
            res.append(''.join(tmp))
            tmp=[]
        else:
            tmp.append(i)
    else:
        if i == '<':
            tmp.reverse()
            res.append(''.join(tmp))
            tmp=[i]
        elif i == ' ':
            tmp.reverse()
            res.append(''.join(tmp))
            res.append(' ')
            tmp=[]
        else:
            tmp.append(i)
if tmp:
    if tmp[0]=='<':
        res.append(''.join(tmp))
    else:
        tmp.reverse()
        res.append(''.join(tmp))
print(''.join(res))