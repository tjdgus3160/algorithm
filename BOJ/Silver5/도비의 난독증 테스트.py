# 2204번
import sys
input=sys.stdin.readline

res=[]
while True:
    n=int(input())
    if n == 0:
        break
    arr=[]
    for i in range(n):
        word=input().rstrip('\n')
        tmp="".join(map(lambda x:x.lower(),word))
        arr.append((tmp,word))
    arr.sort()
    res.append(arr[0][1])
for i in res:
    print(i)