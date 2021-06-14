# 14582번
import sys
input=sys.stdin.readline

a=[*map(int,input().split())]
b=[*map(int,input().split())]
flag=False
res='No'
aa,bb=0,0
for i in range(9):
    aa+=a[i]
    if aa>bb:
        flag=True
    bb+=b[i]
    if flag and bb>aa:
        res='Yes'
print(res)