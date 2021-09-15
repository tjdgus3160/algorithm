# 17144번
import sys
input=sys.stdin.readline

def spread(x,y):
    tmp=[]
    for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if 0<=nx<r and 0<=ny<c and arr[nx][ny]!=-1:
            tmp.append((nx,ny))
    if tmp:
        k=arr[x][y]//5
        _arr[x][y]+=arr[x][y]-k*len(tmp)
        for nx,ny in tmp:
            _arr[nx][ny]+=k

def func():
    for x in range(clear[0]-1,0,-1):
        _arr[x][0]=_arr[x-1][0]
    _arr[0][:-1]=_arr[0][1:]
    for x in range(clear[0]):
        _arr[x][-1]=_arr[x+1][-1]
    _arr[clear[0]][1:]=[0]+_arr[clear[0]][1:-1]

    for x in range(clear[1]+1,r-1):
        _arr[x][0]=_arr[x+1][0]
    _arr[-1][:-1]=_arr[-1][1:]
    for x in range(r-1,clear[1],-1):
        _arr[x][-1]=_arr[x-1][-1]
    _arr[clear[1]][1:]=[0]+_arr[clear[1]][1:-1]

r,c,t=map(int,input().split())
arr=[]
clear=[]
for i in range(r):
    tmp=[*map(int,input().split())]
    if tmp[0]==-1:
        clear.append(i)
    arr.append(tmp)

for _ in range(t):
    _arr=[[0]*c for _ in range(r)]
    for i in clear:
        _arr[i][0]=-1
    for i in range(r):
        for j in range(c):
            if arr[i][j]>0:
                spread(i,j)
    func()
    arr=[i[:] for i in _arr]
print(sum([sum(i) for i in arr])+2)