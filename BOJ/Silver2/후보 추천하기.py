# 1713번
import sys
input=sys.stdin.readline

n=int(input())
input()
arr=[*map(int,input().split())]
res=[]
s=set()
for idx,i in enumerate(arr):
    if i in s:
        for j in range(len(res)):
            if res[j][0]==i:
                res[j][1]+=1
                break
    else:
        if len(s)<n:
            s.add(i)
            res.append([i,1,idx])
        else:
            res.sort(key=lambda x:(-x[1],-x[2]))
            v,_,_=res.pop()
            s.remove(v)
            res.append([i, 1, idx])
            s.add(i)
print(*sorted([i[0] for i in res]))
