# 9536번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    arr=input().split()
    sound=set()
    while True:
        s=input().rstrip('\n')
        if s=='what does the fox say?':
            break
        _,_,k=s.split()
        sound.add(k)
    print(*[i for i in arr if i not in sound])