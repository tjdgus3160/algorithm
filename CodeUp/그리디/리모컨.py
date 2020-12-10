import sys
input=sys.stdin.readline


a,b=map(int,input().split())
t=abs(a-b)

l=[0,1,2,3,2,1,2,3,3,2]
cnt=t//10
cnt+=l[t%10]
print(cnt)
