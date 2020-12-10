h,m=map(int,input().split())
if m <30:
    m+=30
    h=(h-1)
else:
    m-=30
if h<0:
    h=23
print(h,m)
