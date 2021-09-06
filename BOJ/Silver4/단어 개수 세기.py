# 19844번
import re
import sys
input=sys.stdin.readline

s=input().rstrip().replace('-',' ')
arr=s.split(' ')
res=len(arr)
for i in arr:
    if re.findall("^(c|j|n|m|t|s|l|d|qu|s)'[aeiouh]",i):
        res+=1
print(res)

