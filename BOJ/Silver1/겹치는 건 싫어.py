import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr=[*map(int,input().split())]
dic={}
start=0
res=0
for i in range(n):
    if arr[i] not in dic:
        dic[arr[i]]=1
    else:
        dic[arr[i]]+=1
        if dic[arr[i]]>k:
            res=max(res,i-start)
            while True:
                dic[arr[start]] -= 1
                start += 1
                if arr[start-1]==arr[i]:
                    break
res=max(res,n-start)
print(res)
