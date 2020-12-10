import sys
input=sys.stdin.readline

res=0
for i in range(int(input())):
    a, b = map(int, input().split())
    res+=b%a
print(res)

