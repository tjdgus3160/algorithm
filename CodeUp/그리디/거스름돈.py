import sys
input=sys.stdin.readline

l=[50000,10000,5000,1000,500,100,50,10]
n=int(input())
cnt=0
for i in l:
    if n>=i:
        cnt+=n//i
        n%=i
print(cnt)
