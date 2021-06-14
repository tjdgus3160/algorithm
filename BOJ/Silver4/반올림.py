# 4539번
import math
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    x=int(input())
    if x<10:
        print(x)
    else:
        for i in range(len(str(x))-1):
            if int(str(x)[-1-i])==5:
                x+=5*pow(10,i)
            x=round(x,-1-i)
        print(x)