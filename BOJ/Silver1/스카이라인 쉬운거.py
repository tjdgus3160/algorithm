import sys
input=sys.stdin.readline

res=0
arr=[]
for _ in range(int(input())):
    x,y=map(int,input().split())
    while arr and arr[-1] > y:
        arr.pop()
    if y and (not arr or arr[-1]<y):
        arr.append(y)
        res+=1
print(res)