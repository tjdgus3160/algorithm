# 5397번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    s=input().rstrip('\n')
    arr1=[]
    arr2=[]
    for i in s:
        if i == '<':
            if arr1:
                arr2.append(arr1.pop())
        elif i == '>':
            if arr2:
                arr1.append(arr2.pop())
        elif i == '-':
            if arr1:
                arr1.pop()
        else:
            arr1.append(i)
    print(''.join(arr1+list(reversed(arr2))))