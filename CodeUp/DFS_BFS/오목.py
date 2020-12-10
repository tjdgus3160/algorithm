import sys
input=sys.stdin.readline

arr=[]
for i in range(19):
    arr.append([*map(int,input().split())])
res=0
loc=[]
flag=False
for y in range(19):
    for x in range(19):
        if arr[y][x]==0:
            continue
        k=arr[y][x]
        if x<18 and arr[y][x+1]==k:
            cnt=2
            xx=x+2
            while True:
                if xx <= 18 and arr[y][xx]==k:
                    xx+=1
                    cnt+=1
                else:
                    break
            if cnt==5:
                if x==0 or arr[y][x-1]!=k:
                    flag=True
                    res=k
                    loc=[y+1,x+1]
                    break
        if x>0 and arr[y][x-1]==k:
            cnt=2
            xx=x-2
            while True:
                if xx>=0 and arr[y][xx]==k:
                    xx-=1
                    cnt+=1
                else:
                    break
            if cnt==5:
                if x==18 or arr[y][x+1]!=k:
                    flag=True
                    res=k
                    loc=[y+1,x-3]
                    break
        if y<18 and arr[y+1][x]==k:
            cnt=2
            yy=y+2
            while True:
                if yy <= 18 and arr[yy][x]==k:
                    yy+=1
                    cnt+=1
                else:
                    break
            if cnt==5:
                if y==0 or arr[y-1][x]!=k:
                    flag=True
                    res=k
                    loc=[y+1,x+1]
                    break
        if y>0 and arr[y-1][x]==k:
            cnt=2
            yy=y-2
            while True:
                if yy>=0 and arr[yy][x]==k:
                    yy-=1
                    cnt+=1
                else:
                    break
            if cnt==5:
                if y==18 or arr[y+1][x]!=k:
                    flag=True
                    res=k
                    loc=[y-3,x+1]
                    break
        if y>0 and x>0 and arr[y-1][x-1]==k:
            cnt=2
            xx=x-2
            yy=y-2
            while True:
                if xx>=0 and yy>=0 and arr[yy][xx]==k:
                    yy-=1
                    xx-=1
                    cnt+=1
                else:
                    break
            if cnt==5:
                if (y==18 and x==18) or arr[y+1][x+1]!=k:
                    flag=True
                    res=k
                    loc=[y-3,x-3]
                    break
        if y>0 and x<18 and arr[y-1][x+1]==k:
            cnt=2
            xx=x+2
            yy=y-2
            while True:
                if yy>=0 and xx<=18 and arr[yy][xx]==k:
                    yy-=1
                    xx+=1
                    cnt+=1
                else:
                    break
            if cnt==5:
                if (x==0 and y==18) or arr[y+1][x-1]!=k:
                    flag=True
                    res=k
                    loc=[y+1,x+1]
                    break
        if y<18 and x<18 and arr[y+1][x+1]==k:
            cnt=2
            xx=x+2
            yy=y+2
            while True:
                if yy<=18 and xx<=18 and arr[yy][xx]==k:
                    yy+=1
                    xx+=1
                    cnt+=1
                else:
                    break
            if cnt==5:
                if (x==0 and y==0) or arr[y-1][x-1]!=k:
                    flag=True
                    res=k
                    loc=[y+1,x+1]
                    break
        if y<18 and x>0 and arr[y+1][x-1]==k:
            cnt=2
            xx=x-2
            yy=y+2
            while True:
                if yy<=18 and xx>=0 and arr[yy][xx]==k:
                    yy+=1
                    xx-=1
                    cnt+=1
                else:
                    break
            if cnt==5:
                if (y==0 and x==18) or arr[y-1][x+1]!=k:
                    flag=True
                    res=k
                    loc=[y+5,x-3]
                    break
    if flag:
        break
if res==0:
    print(0)
else:
    print(res)
    print(*loc)
