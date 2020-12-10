# 2437번
n=int(input())
l=sorted([*map(int,input().split())])
result=1
for i in l:
    if result<i:
        break
    result+=i
print(result)
