import sys
input=sys.stdin.readline

arr=[*map(int,input().split())]
res=0
while arr.count(max(arr))!=3:
    arr.sort()
    if arr[1]<arr[2]:
        arr[0]+=1
        arr[1]+=1
    else:
        arr[0]+=2
    res+=1
print(res)

