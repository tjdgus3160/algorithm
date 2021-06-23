# 17609번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    s=input().rstrip()
    if s==s[::-1]:
        print(0)
    else:
        for i in range(len(s)//2):
            j=len(s)-1-i
            if s[i]!=s[j]:
                tmp1=s[:i]+s[i+1:]
                tmp2=s[:j]+s[j+1:]
                if tmp1==tmp1[::-1] or tmp2==tmp2[::-1]:
                    print(1)
                    break
                else:
                    print(2)
                    break