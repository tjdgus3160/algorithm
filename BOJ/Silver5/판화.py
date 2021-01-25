# 1730번
import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    arr.append(['.']*n)
s=input().rstrip('\n')
x,y=0,0
for v in s:
    if v=='U':
        if 0<=y-1<n:
            if arr[y][x]=='.':
                arr[y][x]='|'
            elif arr[y][x]=='-':
                arr[y][x]='+'
            y-=1
            if arr[y][x] == '.':
                arr[y][x] = '|'
            elif arr[y][x] == '-':
                arr[y][x] = '+'
    elif v=='D':
        if 0<=y+1<n:
            if arr[y][x]=='.':
                arr[y][x]='|'
            elif arr[y][x]=='-':
                arr[y][x]='+'
            y+=1
            if arr[y][x] == '.':
                arr[y][x] = '|'
            elif arr[y][x] == '-':
                arr[y][x] = '+'
    elif v=='L':
        if 0<=x-1<n:
            if arr[y][x]=='.':
                arr[y][x]='-'
            elif arr[y][x]=='|':
                arr[y][x]='+'
            x-=1
            if arr[y][x] == '.':
                arr[y][x] = '-'
            elif arr[y][x] == '|':
                arr[y][x] = '+'
    elif v=='R':
        if 0<=x+1<n:
            if arr[y][x]=='.':
                arr[y][x]='-'
            elif arr[y][x]=='|':
                arr[y][x]='+'
            x+=1
            if arr[y][x] == '.':
                arr[y][x] = '-'
            elif arr[y][x] == '|':
                arr[y][x] = '+'
for i in arr:
    print("".join(i))