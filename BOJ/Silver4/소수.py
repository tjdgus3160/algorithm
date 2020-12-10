# 2581번
m=int(input())
n=int(input())
l=[i for i in range(m,n+1)]
for i in range(2,n+1):
    j=i*2
    while j <= n:
        if j in l:
            l.remove(j)
        j+=i
if m<=1:
    l.remove(1)
if l:
    print(sum(l))
    print(l[0])
else:
    print(-1)