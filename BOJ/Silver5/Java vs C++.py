# 3613번
import sys
input=sys.stdin.readline

s=input().rstrip('\n')
if '_' in s:
    s=s.split('_')
    for i in s:
        if i.lower() != i:
            print('Error!')
            exit()
    res=[]
    for i in range(len(s)):
        if not s[i].isalpha() or (i==0 and s[i][0].isupper()):
            print('Error!')
            exit()
        if i==0:
            res.append(s[i])
        else:
            k=s[i][0].upper()
            if len(s[i])>1:
                k+=s[i][1:]
            res.append(k)
    print(''.join(res))
else:
    for i in range(len(s)):
        if i==0 and s[i].isupper():
            print('Error!')
            exit()
        if s[i].isupper():
            break
    else:
        print(s)
        exit()
    res=[]
    tmp=[]
    for i in s:
        if i.isupper():
            res.append(''.join(tmp))
            tmp=[i.lower()]
        else:
            tmp.append(i)
    if tmp:
        res.append(''.join(tmp))
    print('_'.join(res))