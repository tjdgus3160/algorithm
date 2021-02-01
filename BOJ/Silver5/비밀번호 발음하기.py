# 4659번
import sys
input=sys.stdin.readline

while True:
    s=input().rstrip('\n')
    if s=='end':
        break
    flag=True
    if not [i for i in s if i in 'aeiou']:
        flag=False
    cnt=0
    for i in s:
        if i in 'aeiou':
            if cnt<1:
                cnt=1
            else:
                cnt+=1
        else:
            if cnt>-1:
                cnt=-1
            else:
                cnt-=1
        if cnt>2 or cnt<-2:
            flag=False
            break

    tmp=[chr(ord('a')+j)*2 for j in range(26) if j!=4 and j!=14]
    if [i for i in tmp if i in s]:
        flag=False
    if flag:
        print("<%s> is acceptable."%(s))
    else:
        print("<%s> is not acceptable."%(s))