# 12919번
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

def func(t,s):
    if t==s:
        print(1)
        exit()
    if len(t)>1 and t[-1]=='A':
        func(t[:-1],s)
    if len(t)>1 and t[0]=='B':
        tmp=t[1:]
        func(tmp[::-1],s)

s=input().rstrip()
t=input().rstrip()
func(t,s)
print(0)