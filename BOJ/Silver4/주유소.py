# 13305번
import sys
input=sys.stdin.readline

n=int(input())
way=[*map(int,input().split())]
city=[*map(int,input().split())]
res=city[0]*way[0]
for i in range(1,n-1):
    if city[i]>city[i-1]:
        city[i]=city[i-1]
    res+=city[i]*way[i]
print(res)