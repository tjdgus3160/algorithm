# 16916번
import re
import sys
input=sys.stdin.readline

p=input().rstrip()
s=input().rstrip()
print(1 if re.findall(s,p) else 0)