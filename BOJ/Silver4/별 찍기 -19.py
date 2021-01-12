# 10994번
import sys
input=sys.stdin.readline

n=int(input())
r=1+4*(n-1)
c=1+4*(n-1)
arr=['*'*c]
for i in range(1,n):
    arr.append('* '*i+' '*(c-4*i)+' *'*i)
    arr.append('* '*i+'*'*(c-4*i)+' *'*i)
for i in arr:
    print("".join(i))
arr.reverse()
for i in arr[1:]:
    print("".join(i))