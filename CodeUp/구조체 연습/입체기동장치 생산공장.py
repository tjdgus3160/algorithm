tmp=[]
for i in range(int(input())):
    tmp.append(list(map(int,input().split())))
tmp.sort()
for i in tmp:
    print(*i)
