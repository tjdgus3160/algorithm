import sys
import operator
input=sys.stdin.readline

dict={}
for i in range(int(input())):
    t=input().split()
    if t[0]=="I":
        dict.setdefault(int(t[1]),[]).insert(0,t[2])
    else:
        if int(t[1]) in dict:
            del dict[int(t[1])][0]
tmp=sorted(dict.items(),key=operator.itemgetter(0))

res=[]
for i in tmp:
    if len(i[1])!=0:
        while len(i[1])>0:
            res.append([i[0],i[1][0]])
            del i[1][0]
for i in [*map(int,input().split())]:
    a,b=res[i-1]
    print(a,b)
