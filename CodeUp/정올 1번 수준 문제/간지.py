import sys
input=sys.stdin.readline

n=int(input())
tmp=["F",9]
tmp[0]=chr(ord("F")+(n-2013)%12)
if ord(tmp[0])>ord("L"):
    tmp[0]=chr(ord(tmp[0]) - 12)
tmp[1]=(9+(n-2013))%10
print("%s%d"%(tmp[0],tmp[1]))
