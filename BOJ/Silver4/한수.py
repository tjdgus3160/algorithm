# 1065번
import sys
input=sys.stdin.readline

def func(x):
    if x<100:
        return True
    arr=[]
    while x>0:
        arr.append(x%10)
        x//=10
    diff=arr[1]-arr[0]
    for i in range(1,len(arr)):
        if diff!=arr[i]-arr[i-1]:
            return False
    return True

n=int(input())
res=0
for i in range(1,n+1):
    if func(i):
        res+=1
print(res)

# 공식 사용 : (i//100 + i%10)==(i//10%10 *2) or i<100 for i in range(1,n+1)))