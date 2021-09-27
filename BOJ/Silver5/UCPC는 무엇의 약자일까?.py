# 15904번
import sys
input=sys.stdin.readline

arr=['C','P','C','U']
for i in input().rstrip():
    if i==arr[-1]:
        arr.pop()
        if not arr:
            print('I love UCPC')
            exit()
print('I hate UCPC')
