# 2941번
import sys
input=sys.stdin.readline

s=input().rstrip('\n')
arr=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in arr:
    if i in s:
        s=s.replace(i,'*',s.count(i))
print(len(s))