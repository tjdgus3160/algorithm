# 1475번
import sys
input=sys.stdin.readline

arr=[1]*10
res=1
n=input()
for i in n:
    if i=='\n':
        continue
    if i not in '69':
        if arr[int(i)]==0:
            res+=1
            arr=list(map(lambda x:x+1,arr))
        arr[int(i)]-=1
    elif i in '69':
        if arr[6]==0 and arr[9]==0:
            res+=1
            arr =list(map(lambda x: x + 1, arr))
        if arr[6]!=0:
            arr[6]-=1
        else:
            arr[9]-=1
print(res)