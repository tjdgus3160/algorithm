# 14405번
import sys
input=sys.stdin.readline

s=input().rstrip('\n')
a=["pi", "ka", "chu"]
tmp=''
for i in s:
    tmp+=i
    if tmp in a:
        tmp=''
print('YES' if not tmp else 'NO')