import sys
input=sys.stdin.readline

tmp=[]
for i in range(5):
    tmp.append(int(input()))
tmp.sort()
print(sum(tmp)//5)
print(tmp[2])
