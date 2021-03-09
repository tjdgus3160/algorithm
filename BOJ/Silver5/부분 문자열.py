# 6550번
import sys
input=sys.stdin.readline

while True:
    s=input().rstrip('\n')
    if len(s)==0:
        break
    s,t=s.split()
    idx=0
    for i in range(len(t)):
        if t[i]==s[idx]:
            idx+=1
            if len(s)== idx:
                break
    if len(s)==idx:
        print('Yes')
    else:
        print('No')