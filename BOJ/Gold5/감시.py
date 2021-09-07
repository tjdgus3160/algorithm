# 15683번
import sys
input=sys.stdin.readline

def spread(x,y,dir,tmp):
    for d in dir:
        if d==0:
            ny=y-1
            while 0<=ny and tmp[ny][x]!=6:
                if not tmp[ny][x]:
                    tmp[ny][x]='#'
                ny-=1
        elif d == 2:
            ny = y + 1
            while ny<n and tmp[ny][x] != 6:
                if not tmp[ny][x]:
                    tmp[ny][x] = '#'
                ny+=1
        elif d == 3:
            nx = x + 1
            while nx < m and tmp[y][nx] != 6:
                if not tmp[y][nx]:
                    tmp[y][nx] = '#'
                nx+=1
        else:
            nx=x-1
            while 0<=nx and tmp[y][nx] != 6:
                if not tmp[y][nx]:
                    tmp[y][nx] = '#'
                nx-=1

def check(arr):
    return sum([i.count(0) for i in arr])

def func(k,arr):
    global res
    if k==len(cctv):
        res=min(res,check(arr))
        return
    x,y=cctv[k]
    if arr[y][x]==1:
        for d in range(4):
            tmp=[i[:] for i in arr]
            spread(x,y,[d],tmp)
            func(k+1,tmp)
    elif arr[y][x]==2:
        tmp = [i[:] for i in arr]
        spread(x, y, [0,2], tmp)
        func(k + 1, tmp)
        tmp = [i[:] for i in arr]
        spread(x, y, [1,3], tmp)
        func(k + 1, tmp)
    elif arr[y][x]==3:
        for d in range(4):
            tmp=[i[:] for i in arr]
            dir=[d]+[(d+1)%4]
            spread(x,y,dir,tmp)
            func(k+1,tmp)
    elif arr[y][x]==4:
        for d in range(4):
            tmp=[i[:] for i in arr]
            dir=[0,1,2,3]
            dir.remove(d)
            spread(x,y,dir,tmp)
            func(k+1,tmp)
    else:
        tmp = [i[:] for i in arr]
        spread(x,y,[0,1,2,3],tmp)
        func(k + 1, tmp)

n,m=map(int,input().split())
arr=[]
cctv=[]
for y in range(n):
    tmp=[*map(int,input().split())]
    for x in range(m):
        if 0<tmp[x]<6:
            cctv.append((x,y))
    arr.append(tmp)
res=float('inf')
func(0,arr)
print(res)