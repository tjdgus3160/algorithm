# 4378번
import sys
input=sys.stdin.readline

arr=['`1234567890-=','QWERTYUIOP[]\\','ASDFGHJKL;\'','ZXCVBNM,./']
while True:
    s=input().rstrip('\n')
    if not s:
        break
    res=[]
    for i in s:
        for sub in arr:
            if i in sub:
                k=(sub.index(i)-1)%len(sub)
                res.append(sub[k])
                break
        else:
            res.append(i)
    print(''.join(res))