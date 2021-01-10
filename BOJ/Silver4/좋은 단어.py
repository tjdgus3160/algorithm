# 3986번
import sys
input=sys.stdin.readline

arr=[]
res=0
for _ in range(int(input())):
    arr.append(input().rstrip('\n'))
for word in arr:
    tmp=[]
    for s in word:
        if not tmp:
            tmp.append(s)
            continue
        if tmp[-1]==s:
            tmp.pop()
        else:
            tmp.append(s)
    if not tmp:
        res+=1
print(res)
