# 11478번
import sys
input=sys.stdin.readline

tmp={}
s=input().rstrip('\n')
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        k=s[i:j]
        if k not in tmp:
            tmp[k]=1
print(len(tmp))