import sys
input=sys.stdin.readline

cnt=0
def func(tot,k):
    global cnt,isused
    if tot==n:
        cnt+=1
        return
    if tot>n:
        return
    for i in range(1,4):
        if i==3:
            if k>0:
                func(tot+i,-1)
        else:
            func(tot+i,k+1)

n=int(input())
func(0,1)
print(cnt)
