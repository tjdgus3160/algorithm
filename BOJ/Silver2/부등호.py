# 2529번
import copy
import sys
input=sys.stdin.readline

def big(k,tmp):
    global res
    if k==n:
        if len(tmp)==n+1:
            cp=copy.deepcopy(tmp)
            res[0]=cp
        return
    for i in range(9,-1,-1):
        if res[0]!=0:
            return
        if i in tmp:
            continue
        if arr[k]=='<' and tmp[-1]<i:
            tmp.append(i)
            big(k+1,tmp)
            tmp.pop()
        if arr[k]=='>' and tmp[-1]>i:
            tmp.append(i)
            big(k+1,tmp)
            tmp.pop()

def small(k,tmp):
    global res
    if k==n:
        if len(tmp)==n+1:
            cp=copy.deepcopy(tmp)
            res[1]=cp
        return
    for i in range(10):
        if res[1]!=0:
            return
        if i in tmp:
            continue
        if arr[k]=='<' and tmp[-1]<i:
            tmp.append(i)
            small(k+1,tmp)
            tmp.pop()
        if arr[k]=='>' and tmp[-1]>i:
            tmp.append(i)
            small(k + 1, tmp)
            tmp.pop()

n=int(input())
arr=input().split()
res=[0,0]
for i in range(10):
    small(0,[i])
for i in range(9,-1,-1):
    big(0,[i])
for sub in res:
    print(''.join(map(str,sub)))