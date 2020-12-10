import sys
input=sys.stdin.readline

tmp=[]
for i in range(3):
    tmp.append([*map(int,input().split())])

for i in tmp:
    t=i.count(0)
    if t==1:
        print("A")
    elif t==2:
        print("B")
    elif t==3:
        print("C")
    elif t==4:
        print("D")
    else:
        print("E")
