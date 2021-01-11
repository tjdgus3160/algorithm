# 10825번
import sys
input=sys.stdin.readline

arr=[]
for _ in range(int(input())):
    n,k,e,m=input().split()
    arr.append([n,int(k),int(e),int(m)])
arr.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in arr:
    print(i[0])