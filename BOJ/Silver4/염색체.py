# 9342번
import re
import sys
input=sys.stdin.readline

p= "[A-F]?A+F+C+[A-F]?$"
for _ in range(int(input())):
    s=input().rstrip()
    print('Infected!' if re.match(p,s) else 'Good')

