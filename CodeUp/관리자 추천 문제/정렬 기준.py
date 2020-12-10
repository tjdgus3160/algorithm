import sys
input=sys.stdin.readline

tmp=[]
for i in range(int(input())):
    tmp.append([i+1,*map(int,input().split())])
tmp.sort(key=lambda x:(-x[1],-x[2],x[0]))
for i in tmp:
    print(*i)
