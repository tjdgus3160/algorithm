# 11723번
import sys
input=sys.stdin.readline

s=[False]*21
for _ in range(int(input())):
    cmd=list(input().split())
    if cmd[0]=='add':
        s[int(cmd[1])]=True
    elif cmd[0]=='remove':
        s[int(cmd[1])]=False
    elif cmd[0]=='check':
        print(1 if s[int(cmd[1])] else 0)
    elif cmd[0]=='toggle':
        s[int(cmd[1])]= not s[int(cmd[1])]
    elif cmd[0]=='all':
        s = [True] * 21
    elif cmd[0]=='empty':
        s = [False] * 21