# 3568번
import sys
input=sys.stdin.readline

s=input().rstrip('\n').split()
head=s.pop(0)
for v in s:
    var=""
    tmp=[]
    for i in v:
        if i in ',;[':
            continue
        elif i == ']':
            tmp.append('[]')
        elif i == '&':
            tmp.append(i)
        elif i == '*':
            tmp.append(i)
        else:
            var+=i
    tmp.reverse()
    print("%s%s %s;"%(head,"".join(tmp),var))
