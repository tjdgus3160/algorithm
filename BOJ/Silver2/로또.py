# 6603번
from itertools import combinations
import sys
input=sys.stdin.readline

while True:
    a=input().rstrip('\n')
    if a=='0':
        break
    k,*arr=a.split()
    for sub in combinations(arr,6):
        print(*sub)
    print()