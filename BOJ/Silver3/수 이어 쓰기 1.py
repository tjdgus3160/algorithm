# 1748번
import sys
input=sys.stdin.readline

n=int(input())
res=0
for i in range(1,len(str(n))):
    res+=(i*(10**i-(10**(i-1))))
if n<10:
    res+=n
else:
    res+=(len(str(n))*(n-(10**(len(str(n))-1)-1)))
print(res)
