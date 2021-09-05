import sys
input=sys.stdin.readline

r,c=map(int,input().split())
arr=[input().rstrip() for _ in range(r)]

res=[]
for i in arr:
    res.extend([j for j in i.split('#') if len(j)>1])
arr = list(map(lambda x: ''.join(x), zip(*arr)))
for i in arr:
    res.extend([j for j in i.split('#') if len(j)>1])
print(sorted(res)[0])
