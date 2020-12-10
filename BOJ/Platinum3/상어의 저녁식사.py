# 1671번
def find(x):
    for i in a[x]:
        if c[i]:
            continue
        c[i]=1
        if d[i]==0 or find(d[i]):
            d[i]=x
            return True
    return False

n=int(input())
l=[[]]
for _ in range(n):
    l.append(list(map(int,input().split())))

a=[[] for _ in range(n+1)]
for i in range(1,n):
    for j in range(i+1,n+1):
        if l[i][0]==l[j][0] and l[i][1]==l[j][1] and l[i][2]==l[j][2]:
            a[i].append(j)
        elif l[i][0]<=l[j][0] and l[i][1]<=l[j][1] and l[i][2]<=l[j][2]:
            a[j].append(i)
        elif l[i][0]>=l[j][0] and l[i][1]>=l[j][1] and l[i][2]>=l[j][2]:
            a[i].append(j)

d=[0]*(n+1)
cnt=0
for _ in range(2):
    for i in range(1,n+1):
        c=[0]*(n+1)
        if find(i):
            cnt+=1
print(n-cnt)