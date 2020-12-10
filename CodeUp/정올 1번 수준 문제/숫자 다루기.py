import sys
input=sys.stdin.readline

a=list(input())
if a[-1]=="\n":
    del a[-1]
a.reverse()
print(int("".join(a)))
print(sum(list(map(int,a))))

