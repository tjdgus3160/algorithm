a=[]
n=int(input())
for _ in range(n-1):
    a.append(int(input()))
for i in range(1,n+1):
    if i not in a:
        print(i)
        break
