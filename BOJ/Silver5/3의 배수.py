# 1769번
import sys
input=sys.stdin.readline

n=input()[:-1]
res=0
while len(n)>1:
    tmp=0
    for i in n:
        tmp+=int(i)
    n=str(tmp)
    res+=1
print(res)
print("YES" if n in '369' else "NO")