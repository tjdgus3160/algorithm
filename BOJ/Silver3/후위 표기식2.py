# 1935번
import sys
input=sys.stdin.readline

n=int(input())
exp=list(input().rstrip('\n'))
l=[]
dic={}
for i in range(n):
    v=int(input())
    dic[chr(ord('A') +i)]=v

while exp:
    s = exp.pop(0)
    if s in "+-*/":
        b = l.pop()
        a = l.pop()
        l.append(eval(str(a) + s + str(b)))
    else:
        l.append(dic[s])

print("%.2f"%(l[0]))