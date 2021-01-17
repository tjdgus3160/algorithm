# 1072번
# hint y/x*100 은 숫자가 큰 경우 오차가 발생할 수 있음으로 100*y/x로 연산 실행
import sys
input=sys.stdin.readline

def bisearch(x,y,n):
    z=int(100*y/x)
    start=0
    end=n
    res=0
    while start<=end:
        mid=(start+end)//2
        if z+1<=int(100*(y+mid)/(x+mid)):
            end=mid-1
            res=mid
        else:
            start=mid+1
    return res

x,y=map(int,input().split())
if int(100*y/x)>98:
    print(-1)
else:
    print(bisearch(x,y,x))