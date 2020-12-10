import sys
input=sys.stdin.readline

tmp=[]
for i in range(7):
    tmp.append(int(input()))
tmp.sort(reverse=True)
print(tmp[0])
print(tmp[1])
