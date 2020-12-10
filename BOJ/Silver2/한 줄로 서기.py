# 1138번
n=int(input())
w=list(map(int,input().split()))
result=[]
for i in range(n):
    for j in range(n):
        if j+1 in result:
            continue
        if w[j]==0:
            result.append(j+1)
            break
        else:
            w[j]-=1
print(*result)