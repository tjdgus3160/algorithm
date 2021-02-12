def solution(n):
    arr=[[0]*i for i in range(1,n+1)]
    d=0 # 0아래 1우측 2위
    total=sum([*range(1,n+1)])
    x,y=0,0
    cur=1
    while True:
        if not arr[y][x]:
            arr[y][x]=cur
        cur+=1
        if cur>total:
            break
        if d==0:
            if len(arr)-1<y+1 or arr[y+1][x]:
                d=1
                x+=1
            else:
                y+=1
        elif d==1:
            if len(arr[y])-1<x+1 or arr[y][x+1]:
                d=2
                y-=1
                x-=1
            else:
                x+=1
        else:
            if 0>y-1 or arr[y-1][x-1]:
                d=0
                y+=1
            else:
                x-=1
                y-=1
    return sum(arr, [])