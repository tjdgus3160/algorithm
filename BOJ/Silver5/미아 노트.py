import sys
input=sys.stdin.readline

n,h,w=map(int,input().split())
arr=[input().rstrip() for _ in range(h)]
res=''
for i in range(n):
    k='?'
    for line in arr:
        tmp=[j for j in line[w*i:w*i+w] if j!='?']
        if tmp:
            k=tmp[0]
    res+=k
print(res)