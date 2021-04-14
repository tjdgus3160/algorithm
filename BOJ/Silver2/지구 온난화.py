# 5212번
import sys
input=sys.stdin.readline

def check(x,y):
    res=0
    if x==0 or arr[y][x-1]=='.':
        res+=1
    if x==c-1 or arr[y][x+1]=='.':
        res+=1
    if y==0 or arr[y-1][x]=='.':
        res+=1
    if y==r-1 or arr[y+1][x]=='.':
        res+=1
    return res>2

r,c=map(int,input().split())
arr=[]
U,D,R,L=99,0,0,99
tmp=[]
for _ in range(r):
    arr.append(list(input().rstrip('\n')))
for y in range(r):
    for x in range(c):
        if arr[y][x]=='X':
            if check(x,y):
                tmp.append((x,y))
            else:
                U=min(U,y)
                D=max(D,y)
                L=min(L,x)
                R=max(R,x)
for x,y in tmp:
    arr[y][x]='.'
for y in range(U,D+1):
    print(''.join(arr[y][L:R+1]))