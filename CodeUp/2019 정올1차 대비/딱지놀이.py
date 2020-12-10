import sys
input=sys.stdin.readline

res=[]
for i in range(int(input())):
    a=[*map(int,input().split())][1:]
    b=[*map(int,input().split())][1:]
    if max(a)>max(b):
        res.append("A")
    elif max(a)<max(b):
        res.append("B")
    else:
        flag=1
        for i in range(4,0,-1):
            if a.count(i)>b.count(i):
                res.append("A")
                flag=0
                break
            elif a.count(i)<b.count(i):
                res.append("B")
                flag=0
                break
        if flag:
            res.append("D")

for i in res:
    print(i)

