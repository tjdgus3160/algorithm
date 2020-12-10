import itertools
import sys
input=sys.stdin.readline

n=list(input())
if n[-1]=="\n":
    del n[-1]
n.reverse()
print("".join(n))


