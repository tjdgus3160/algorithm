# 12101번
import sys
input=sys.stdin.readline

def func(acc,tmp):
    global res
    if acc==n:
        res+=1
        if res==k:
            print('+'.join(map(str,tmp)))
            exit()
        return
    for i in range(1,4):
        if acc+i<=n:
            func(acc+i,tmp+[i])

n,k=map(int,input().split())
res=0
func(0,[])
print(-1)