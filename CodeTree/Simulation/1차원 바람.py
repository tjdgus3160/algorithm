import sys
input=sys.stdin.readline

def move(line,d):
    if d:
        return [line[-1]]+line[:-1]
    else:
        return line[1:]+[line[0]]

n,m,q=map(int,input().split())
arr=[[*map(int,input().split())] for _ in range(n)]
for _ in range(q):
    r,d=input().split()
    r=int(r)-1
    if d=='L':
        d=True
    else:
        d=False
    arr[r]=move(arr[r],d)
    up,down=r-1,r+1
    updir,downdir=not d,not d
    cur=r
    while up>=0:
        if not [True for i,j in zip(arr[cur],arr[up]) if i==j]:
            break
        arr[up]=move(arr[up],updir)
        updir=not updir
        up-=1
        cur-=1
    cur=r
    while down<n:
        if not [True for i,j in zip(arr[cur],arr[down]) if i==j]:
            break
        arr[down]=move(arr[down],downdir)
        downdir=not downdir
        down+=1
        cur+=1
for i in arr:
    print(*i)