# 1002번
import math
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    dist=math.sqrt(pow((x1-x2),2)+pow((y1-y2),2))
    if dist==0:
        if r1==r2:
            print(-1)
        else:
            print(0)
    elif dist<r1:
        if dist+r2<r1:
            print(0)
        elif dist+r2==r1:
            print(1)
        elif dist+r1>r2:
            print(2)
        elif dist+r1==r2:
            print(1)
        else:
            print(0)
    elif dist==r1:
        if dist+r1>r2:
            print(2)
        elif dist+r1==r2:
            print(1)
        else:
            print(0)
    elif dist>r1:
        if r1+r2<dist:
            print(0)
        elif r1+r2==dist:
            print(1)
        elif dist+r1>r2:
            print(2)
        elif dist+r1==r2:
            print(1)
        else:
            print(0)
