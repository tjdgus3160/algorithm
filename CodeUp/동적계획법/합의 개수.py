n=int(input())
l=[1]
for i in range(1,n):
    l.append(l[-1]*i)
result=0
for i in range(n-1):
    result+=l[n-1]//(l[i]*l[n-1-i])
print(result)
