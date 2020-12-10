# 1946번
import sys
input=sys.stdin.readline
INF=sys.maxsize
for _ in range(int(input())):
    l=[]
    for _ in range(int(input())):
        l.append(list(map(int,input().split())))
    l.sort()
    tmp=INF
    cnt=0
    for i in l:
        if i[1]<tmp:
            cnt+=1
            tmp=i[1]
    print(cnt)