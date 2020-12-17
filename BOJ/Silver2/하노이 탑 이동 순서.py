# 11729번
import sys
input=sys.stdin.readline

def move(a,b,n):
    if n==1:
        print(a,b)
        return
    move(a,6-a-b,n-1)
    print(a,b)
    move(6-a-b,b,n-1)

n=int(input())
print((2**n)-1)
move(1,3,n)