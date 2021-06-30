# 1662번
import sys
input=sys.stdin.readline

def func(s):
    res=0
    left=0
    mul=0
    k=0
    for i in range(len(s)):
        if s[i]=='(':
            if not left:
                left=i
                mul=int(s[i-1])
                res -= 1
            else:
                k+=1
        elif s[i]==')':
            if k:
                k-=1
            else:
                res+=mul*func(s[left+1:i])
                left,mul=0,0
        else:
            if not left:
                res+=1
    return res

print(func(input().rstrip()))