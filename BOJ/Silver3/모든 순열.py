# 10974번
from itertools import permutations
import sys
input=sys.stdin.readline

n=int(input())
for sub in permutations([*range(1,n+1)],n):
    print(*sub)