# 10472번
from collections import deque
import copy
import sys
input=sys.stdin.readline

def dfs():
    dq=deque()
    dic={}
    tmp=[]
    if arr[0]==['.','.','.'] and arr[1]==['.','.','.'] and arr[2]==['.','.','.']:
        return 0
    for _ in range(3):
        tmp.append(['.','.','.'])
    dq.append(tmp)
    dic["".join(tmp[0]+tmp[1]+tmp[2])]=1
    res=1
    while True:
        cnt=len(dq)
        for _ in range(cnt):
            bord=dq.popleft()
            for y in range(3):
                for x in range(3):
                    tmp = copy.deepcopy(bord)
                    tmp[y][x]='.' if tmp[y][x]=='*' else '*'
                    for i in range(4):
                        ny=y+dy[i]
                        nx=x+dx[i]
                        if 0<=nx<3 and 0<=ny<3:
                            tmp[ny][nx] = '.' if tmp[ny][nx] == '*' else '*'
                    if tmp[0]==arr[0] and tmp[1]==arr[1] and tmp[2]==arr[2]:
                        return res
                    s="".join(tmp[0]+tmp[1]+tmp[2])
                    if s not in dic:
                        dq.append(tmp)
                        dic[s]=1
        res+=1

dx=[0,0,1,-1]
dy=[1,-1,0,0]
for _ in range(int(input())):
    arr=[]
    for _ in range(3):
        arr.append(list(input().rstrip('\n')))
    print(dfs())