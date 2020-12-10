import sys
input=sys.stdin.readline

def com(a,b):
    k = 0
    for i in range(3,0,-1):
        if dict[a][i]>dict[b][i]:
            k=a
            break
        elif dict[a][i]<dict[b][i]:
            k=b
            break
    return k

a=[]
b=[]
c=[]
dict={1:[0,0,0,0],2:[0,0,0,0],3:[0,0,0,0]}
for i in range(int(input())):
    a1,b1,c1=map(int,input().split())
    a.append(a1)
    dict[1][a1]+=1
    b.append(b1)
    dict[2][b1]+=1
    c.append(c1)
    dict[3][c1]+=1

res=[[sum(a),1],[sum(b),2],[sum(c),3]]
res.sort()
if res[0][0]==res[2][0]:
    k=com(res[0][1],res[1][1])
    if k==0:
        k=com(res[0][1],res[2][1])
    else:
        k=com(k,res[2][1])
    print(k,res[0][0])
elif res[1][0]==res[2][0]:
    k=com(res[1][1],res[2][1])
    print(k,res[2][0])
else:
    res[2].reverse()
    print(*res[2])
