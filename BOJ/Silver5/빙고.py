# 2578번
import sys
input=sys.stdin.readline

def mark(x):
    for sub in arr:
        if x in sub:
            sub[sub.index(x)]=0

def check():
    res=0
    if arr[0][0]==0 and arr[1][1]==0 and arr[2][2]==0 and arr[3][3]==0 and arr[4][4]==0:
        res+=1
    if arr[0][4]==0 and arr[1][3]==0 and arr[2][2]==0 and arr[3][1]==0 and arr[4][0]==0:
        res+=1
    for i in range(5):
        if arr[i][0] == 0 and arr[i][1] == 0 and arr[i][2] == 0 and arr[i][3] == 0 and arr[i][4] == 0:
            res += 1
    for i in range(5):
        if arr[0][i] == 0 and arr[1][i] == 0 and arr[2][i] == 0 and arr[3][i] == 0 and arr[4][i] == 0:
            res += 1
    return res

arr=[]
l=[]
for _ in range(5):
    arr.append([*map(int,input().split())])
for _ in range(5):
    l+=[*map(int,input().split())]
for idx,v in enumerate(l):
    mark(v)
    if check()>=3:
        print(idx+1)
        break