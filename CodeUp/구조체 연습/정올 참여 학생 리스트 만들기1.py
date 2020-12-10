import sys
input=sys.stdin.readline

res=[]
v=[]
for i in range(int(input())):
    t=input().split()
    if t[0]=="I" and t[1] not in v:
        res.append([t[1],t[2]])
        v.append(t[1])
        res.sort(key=lambda x:int(x[0]))
        v.sort(key=lambda x:int(x))
    else:
        if t[1] in v:
            k=v.index(t[1])
            del res[k]
            del v[k]
for i in list(map(int,input().split())):
    print(" ".join(res[i-1]))
