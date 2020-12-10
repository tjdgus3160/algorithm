import sys
input=sys.stdin.readline

a=[*map(int,input().split())]
o=[0]
e=[0]
for i in a:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
o.sort()
e.sort()
print(o[-1]+e[-1])
