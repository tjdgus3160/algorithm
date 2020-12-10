# 11047번
n,k=map(int,input().split())
l=[]
for i in range(n):
    l.append(int(input()))
result=0
l.reverse()
for i in range(n):
    result+= k//l[i]
    k%=l[i]
print(result)
