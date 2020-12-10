# 1331번
import sys
input=sys.stdin.readline

def possi(s):
    apl,num=s[0],int(s[1])
    poss=[]
    if chr(ord(apl)+1)>='A' and chr(ord(apl)+1)<='F':
        if num+2<=6:
            poss.append(chr(ord(apl)+1)+str(num+2))
        if num-2>=1:
            poss.append(chr(ord(apl) + 1) + str(num-2))
    if chr(ord(apl)+2)>='A' and chr(ord(apl)+2)<='F':
        if num+1<=6:
            poss.append(chr(ord(apl)+2)+str(num+1))
        if num-1>=1:
            poss.append(chr(ord(apl)+2) + str(num-1))
    if chr(ord(apl)-1)>='A' and chr(ord(apl)-1)<='F':
        if num+2<=6:
            poss.append(chr(ord(apl)-1)+str(num+2))
        if num-2>=1:
            poss.append(chr(ord(apl)-1)+str(num-2))
    if chr(ord(apl)-2)>='A' and chr(ord(apl)-2)<='F':
        if num+1<=6:
            poss.append(chr(ord(apl)-2)+str(num+1))
        if num-1>=1:
            poss.append(chr(ord(apl)-2) + str(num-1))
    return poss
start=input()
start=list(start)
if start[-1]=="\n":
    del start[-1]
start="".join(start)
v=[start]
res=True
for _ in range(35):
    a=list(input())
    if a[-1]=="\n":
        del a[-1]
    a="".join(a)
    if a not in possi(v[-1]) or a in v:
        res=False
    v.append(a)
if res and v[0] not in possi(v[-1]):
    res=False
print("Valid" if res else "Invalid")