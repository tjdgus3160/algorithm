# 9012번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    s=input().rstrip('\n')
    tmp=[]
    flag=True
    for i in s:
        if i =='(':
            tmp.append(i)
        else:
            if tmp:
                tmp.pop()
            else:
                flag=False
                break
    if flag and not tmp:
        print("YES")
    else:
        print("NO")