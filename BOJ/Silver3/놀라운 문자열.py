# 1972번
import sys
input=sys.stdin.readline

while True:
    s=input().rstrip('\n')
    if s=='*':
        break
    flag=True
    for i in range(len(s)-1):
        tmp=[]
        for j in range(len(s)-i-1):
            k=s[j]+s[j+1+i]
            if k in tmp:
                flag=False
                break
            tmp.append(k)
        else:
            continue
        break
    if flag:
        print('%s is surprising.'%(s))
    else:
        print('%s is NOT surprising.'%(s))