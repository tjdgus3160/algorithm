from itertools import product
import sys
input=sys.stdin.readline

def bom1(x,y):
    return [(x,y),(x,y-1),(x,y-2),(x,y+1),(x,y+2)]

def bom2(x,y):
    return [(x,y),(x,y-1),(x-1,y),(x,y+1),(x+1,y)]

def bom3(x,y):
    return [(x,y),(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1)]

n=int(input())
arr=[]
boom=[]
cnt=0
for y in range(n):
    tmp=[*map(int,input().split())]
    for x in range(n):
        if tmp[x]:
            boom.append((x,y))
            cnt+=1
    arr.append(tmp)
res=0
for sub in product([*range(1,4)],repeat=cnt):
    tmp=[]
    for k,loc in zip(sub,boom):
        if k==1:
            for x,y in bom1(loc[0],loc[1]):
                if 0<=x<n and 0<=y<n and (x,y) not in tmp:
                    tmp.append((x,y))
        elif k==2:
            for x,y in bom2(loc[0],loc[1]):
                if 0<=x<n and 0<=y<n and (x,y) not in tmp:
                    tmp.append((x,y))
        else:
            for x,y in bom3(loc[0],loc[1]):
                if 0<=x<n and 0<=y<n and (x,y) not in tmp:
                    tmp.append((x,y))
    res=max(res,len(tmp))
print(res)