import sys
input=sys.stdin.readline

a,b,c,n=map(int,input().split())

flag=True
for i in range(n):
    tmp=n-(c*i)
    if tmp==0:
        print(1)
        flag = False
        break
    if tmp>=0:
        for j in range(n):
            ttmp=tmp-(b*j)
            if ttmp>=0 and ttmp%a==0:
                print(1)
                flag=False
                break
        if not flag:
            break

if flag:
    print(0)
