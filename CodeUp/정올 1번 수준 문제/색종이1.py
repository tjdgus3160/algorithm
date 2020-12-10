import sys
input=sys.stdin.readline

l=[[0 for i in range(100)] for i in range(100)]

tmp=[]

for i in range(int(input())):
    tmp.append([*map(int,input().split())])
for i in tmp:
    x,y=i
    for j in range(10):
        for k in range(10):
            if l[y+j-1][x+10-k-1]==0:
                l[y+j-1][x+10-k-1]=1
res=0
for i in l:
    res+=sum(i)
print(res)

