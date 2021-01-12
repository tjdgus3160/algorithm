# 13305번
import sys
input=sys.stdin.readline

res=0
n=int(input())
way=[*map(int,input().split())]
city=[*map(int,input().split())]
loc=0
cost=city[0]
while loc<n-2:
    if loc==0:
        if cost>city[loc+1]:
            res+=cost*way[loc]
            loc+=1
        else:
            for i in range(loc+1,n-1):
                if city[i]<=cost:
                    res+=city[i-1]*way[i-1]
                    loc=i
                    break
                else:
                    city[i] =cost
                    res+=cost*way[i]
                    loc = i
    else:
        for i in range(loc+1, n-1):
            if city[i] < city[loc]:
                res += city[i - 1] * way[i - 1]
                loc = i
                break
            else:
                city[i]=city[loc]
                res += city[loc] * way[i-1]
                loc=i
print(res+city[n-2]*way[-1])