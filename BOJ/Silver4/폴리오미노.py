# 1343번
import sys
input=sys.stdin.readline

s=input().rstrip('\n')
cnt=0
res=[]
for i in s:
    if i=='X':
        cnt+=1
    else:
        if cnt==0:
            res.append(i)
        else:
            if cnt==1 or cnt%2==1:
                print(-1)
                exit()
            else:
                while cnt:
                    if cnt>=4:
                        res.append('AAAA')
                        cnt-=4
                    else:
                        res.append('BB')
                        cnt-=2
                res.append('.')
if cnt==1 or cnt%2==1:
    print(-1)
    exit()
while cnt:
    if cnt>=4:
        res.append('AAAA')
        cnt-=4
    else:
        res.append('BB')
        cnt-=2
print(''.join(res))