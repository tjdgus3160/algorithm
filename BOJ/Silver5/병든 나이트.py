# 1783번
n,m=map(int,input().split())
cnt=1
if m<7:
    if n<3:
        cnt+=(m-1)//2
    else:
        cnt+=(m-1)
        if cnt>4:
            cnt=4
else:
    if n<3:
        cnt+=3
    else:
        cnt=cnt+4+(m-7)
if n == 1:
    cnt=1
print(cnt)