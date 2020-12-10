# 1064번
import math
import sys
input=sys.stdin.readline

def dist(arr1,arr2):
    return math.sqrt((arr2[1]-arr1[1])**2+(arr2[0]-arr1[0])**2)

def alis(arr1,arr2):
    try:
        t=(arr2[1]-arr1[1])/(arr2[0]-arr1[0])
    except:
        return 1
    return t

a=[*map(int,input().split())]
dot1=[a[0],a[1]]
dot2=[a[2],a[3]]
dot3=[a[4],a[5]]
if alis(dot1,dot2)==alis(dot1,dot3):
    print(-1)
else:
    t1=dist(dot1,dot2)+dist(dot1,dot3)
    t2=dist(dot1,dot3)+dist(dot3,dot2)
    t3=dist(dot2,dot3)+dist(dot2,dot1)

    tarr=[t1,t2,t3]
    print(2*(max(tarr)-min(tarr)))