# 9576번
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(x):
    for i in range(arr[x][0],arr[x][1]+1):
        if is_match[i]: continue
        is_match[i]=True
        if book[i]==-1 or dfs(book[i]):
            book[i]=x
            return True
    return False

for _ in range(int(input())):
    n,m=map(int,input().split())
    arr=sorted([[*map(lambda x:int(x)-1,input().split())]for _ in range(m)],key=lambda x:abs(x[1]-x[0]))
    res=0
    book=[-1]*n
    for i in range(m):
        is_match=[False]*n
        if dfs(i):
            res+=1
    print(res)