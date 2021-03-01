# 14729번
import sys
input=sys.stdin.readline

arr=[]
for _ in range(int(input())):
    arr.append(input().rstrip('\n'))
    if len(arr)>1000:
        arr.sort(key=lambda x:(len(x),float(x)))
        arr=arr[:7]
arr.sort(key=lambda x: (len(x), float(x)))
for i in arr[:7]:
    print(i)