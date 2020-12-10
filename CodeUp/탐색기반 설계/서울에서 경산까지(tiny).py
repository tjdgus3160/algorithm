import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
INF=sys.maxsize

def find(t,m,city):
    if t>k:
        return 0
    if city==n+1:
        return m
    if time[city-1][0]<time[city-1][1] and cost[city-1][0]>cost[city-1][1]:
        return max(m,find(t+time[city-1][0],m+cost[city-1][0],city+1))
    elif time[city-1][0]>time[city-1][1] and cost[city-1][0]<cost[city-1][1]:
        return max(m,find(t+time[city-1][1],m+cost[city-1][1],city+1))
    else:
        return max(m,find(t+time[city-1][1],m+cost[city-1][1],city+1),find(t+time[city-1][0],m+cost[city-1][0],city+1))
res=0
n,k=map(int,input().split())
time=[]
cost=[]
for i in range(n):
    a, b, c, d = map(int, input().split())
    time.append([a,c])
    cost.append([b,d])
print(find(0,0,1))

