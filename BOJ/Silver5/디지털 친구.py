# 1985번
import copy
import sys
input=sys.stdin.readline

def check(a,b):
    sa=set(a)
    sb=set(b)
    la=list(a)
    lb=list(b)
    for i in range(1,len(la)):
        tmp=copy.deepcopy(la)
        tmp[i-1]=str(int(tmp[i-1])-1)
        tmp[i]=str(int(tmp[i])+1)
        if tmp[0]!='0' and set(tmp)==sb:
            return True
        tmp=copy.deepcopy(la)
        tmp[i-1]=str(int(tmp[i-1])+1)
        tmp[i]=str(int(tmp[i])-1)
        if set(tmp) == sb:
            return True
    for i in range(1,len(lb)):
        tmp = copy.deepcopy(lb)
        tmp[i - 1] =str(int(tmp[i-1])-1)
        tmp[i]=str(int(tmp[i])+1)
        if tmp[0] != '0' and set(tmp) == sa:
            return True
        tmp = copy.deepcopy(lb)
        tmp[i - 1]=str(int(tmp[i-1])+1)
        tmp[i]=str(int(tmp[i])-1)
        if set(tmp) == sa:
            return True
    return False

for _ in range(3):
    a,b=input().split()
    if set(a)==set(b):
        print("friends")
    else:
        if check(a,b):
            print('almost friends')
        else:
            print('nothing')