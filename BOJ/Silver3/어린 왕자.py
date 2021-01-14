# 1004번
import math
import sys
input=sys.stdin.readline

def dist(x1,y1,x2,y2):
    return math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    res=0
    for _ in range(int(input())):
        x,y,r=map(int,input().split())
        if dist(x1,y1,x,y)<r and dist(x2,y2,x,y)>r:
            res+=1
        elif dist(x2,y2,x,y)<r and dist(x1,y1,x,y)>r:
            res+=1
    print(res)