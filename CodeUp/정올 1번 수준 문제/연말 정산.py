from math import gcd
import sys
input=sys.stdin.readline

n=int(input())
if n<=500:
    print(int(n*0.7))
elif n<=1500:
    print(350+int((n-500)*0.4))
elif n<=4500:
    print(750+int((n-1500)*0.15))
elif n<=10000:
    print(1200+int((n-4500)*0.05))
else:
    print(1475+int((n-10000)*0.02))
