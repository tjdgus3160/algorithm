# 11652번
import sys
input=sys.stdin.readline

dic={}
for i in range(int(input())):
    n=int(input())
    dic.setdefault(n,0)
    dic[n]+=1
arr=list(dic.items())
arr.sort(key=lambda x:(-x[1],x[0]))
print(arr[0][0])