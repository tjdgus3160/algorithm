# 8896번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    arr=[]
    n=int(input())
    for i in range(1,n+1):
        arr.append([i,list(input().rstrip('\n'))])
    for i in range(len(arr[0][1])):
        sub=[s[1][i] for s in arr]
        if len(set(sub))==2:
            if 'R' not in set(sub):
                arr=[s for s in arr if s[1][i]!='P']
            elif 'S' not in set(sub):
                arr=[s for s in arr if s[1][i]!='R']
            elif 'P' not in set(sub):
                arr = [s for s in arr if s[1][i] != 'S']
        if not arr:
            break
    if len(arr)>1:
        print(0)
    else:
        print(arr[0][0])