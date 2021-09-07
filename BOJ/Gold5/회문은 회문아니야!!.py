# 15927번
import sys
input=sys.stdin.readline

s=input().rstrip()
if len(set(list(s)))==1:
    print(-1)
elif s!=s[::-1]:
    print(len(s))
else:
    print(len(s)-1)