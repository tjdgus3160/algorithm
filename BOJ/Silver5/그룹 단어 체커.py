# 1316번
import sys
input=sys.stdin.readline

def find(s):
    res=True
    v=[]
    for i in range(len(s)):
        if i==0:
            v.append(s[i])
            continue
        if s[i]!=s[i-1] and s[i] in v:
            res=False
            break
        if s[i] not in v:
            v.append(s[i])
    return res

res=0
for i in range(int(input())):
    s=input()
    if find(s):
        res+=1
print(res)