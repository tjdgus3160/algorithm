# 4096번
import sys
input=sys.stdin.readline

while True:
    s=input().rstrip('\n')
    if s=='0':
        break
    cnt=0
    s=[*map(int,list(s))]
    while True:
        k=[1 for i in range(len(s)//2+1) if s[i]!=s[len(s)-1-i]]
        if not k:
            break
        cnt+=1
        s[-1]+=+1
        for i in range(len(s)-1,0,-1):
            if s[i]==10:
                s[i-1]+=1
                s[i]=0
            else:
                break
    print(cnt)