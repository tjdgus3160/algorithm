# 1059번
import bisect
import sys
input=sys.stdin.readline

input()
l=[*map(int,input().split())]
n=int(input())
l.sort()
if n in l:
    print(0)
else:
    k=bisect.bisect_left(l,n)
    if k==0:
        up=l[k]-n
        down=n-1
        print(up - 1 + down * (up))
    else:
        up=l[k]-n
        down=n-l[k-1]-1
        print(up-1+down*(up))