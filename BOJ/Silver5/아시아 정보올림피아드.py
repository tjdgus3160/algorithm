# 2535번
import sys
input=sys.stdin.readline

arr=[]
for _ in range(int(input())):
    arr.append([*map(int,input().split())])
arr.sort(key=lambda x:-x[2])
res=[]
for a,b,_ in arr:
    if len(res)<2:
        res.append([a,b])
    else:
        if res[0][0]!=res[1][0]:
            res.append([a,b])
            break
        else:
            if res[1][0]!=a:
                res.append([a,b])
                break
for i in res:
    print(*i)