# 1302번
import sys
input=sys.stdin.readline

dic={}
for _ in range(int(input())):
    s=input().rstrip("\n")
    if s not in dic:
        dic.setdefault(s,1)
    else:
        dic[s]+=1
print(sorted(dic.items(),key=lambda x:(-x[1],x[0]))[0][0])
