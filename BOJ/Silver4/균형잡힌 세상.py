# 4949번
import sys
input=sys.stdin.readline

while True:
    s=input().rstrip('\n')
    if s=='.':
        break
    tmp=[]
    flag=True
    for i in s:
        if i in "([":
            tmp.append(i)
        elif i==")":
            if len(tmp) and tmp[-1]=='(':
                tmp.pop()
            else:
                flag=False
                break
        elif i=="]":
            if len(tmp) and tmp[-1]=='[':
                tmp.pop()
            else:
                flag=False
                break
    print("yes" if flag and not tmp else "no")