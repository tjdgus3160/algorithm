# 2870번
import sys
input=sys.stdin.readline

def func(s):
    tmp = ""
    for i in s:
        if i.isdigit():
            tmp+=i
            continue
        if tmp:
            res.append(int(tmp))
            tmp=""
    if tmp:
        res.append(int(tmp))

res=[]
for _ in range(int(input())):
    s=input()
    func(s)
res.sort()
for i in res:
    print(i)