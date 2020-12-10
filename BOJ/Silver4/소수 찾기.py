# 1978번
l=[True for _ in range(1001)]
l[1]=False
for i in range(2,int(1000**0.5)+1):
    if l[i]:
        j=i+i
        while j<=1000:
            l[j]=False
            j+=i
input()
result=0
for i in [*map(int,input().split())]:
    if l[i]:
        result+=1
print(result)