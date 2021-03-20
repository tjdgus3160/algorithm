# 2504번
import sys
input=sys.stdin.readline

s=input().rstrip('\n')
arr=[]
try:
    for i in s:
        if i ==')':
            k=0
            while arr[-1] != '(':
                k+=arr.pop()
            arr.pop()
            if k:
                arr.append(k*2)
            else:
                arr.append(2)
        elif i ==']':
            k=0
            while arr[-1] != '[':
                k+=arr.pop()
            arr.pop()
            if k:
                arr.append(k*3)
            else:
                arr.append(3)
        else:
            arr.append(i)
    print(sum(arr))
except:
    print(0)