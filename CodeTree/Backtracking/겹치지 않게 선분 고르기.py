import sys
input=sys.stdin.readline

def func(idx,tmp):
    global res
    res=max(res,len(tmp))
    if idx==-1:
        for i in range(n):
            func(i,tmp+[arr[i]])
    else:
        for i in range(idx+1,n):
            for s,e in tmp:
                if not (arr[i][0]>e or arr[i][1]<s):
                    break
            else:
                func(i,tmp+[arr[i]])

n=int(input())
arr=[[*map(int,input().split())] for _ in range(n)]
res=0
func(-1,[])
print(res)