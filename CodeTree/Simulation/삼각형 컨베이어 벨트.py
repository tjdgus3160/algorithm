n,t=map(int,input().split())
arr=[]
for _ in range(3):
    arr.extend([*map(int,input().split())])
t=t%(3*n)
arr=arr[-t:]+arr[:-t]
print(*arr[:n])
print(*arr[n:2*n])
print(*arr[2*n:])