# 10384번
from collections import defaultdict
import sys
input=sys.stdin.readline

for v in range(int(input())):
    s=input().rstrip()
    dic=defaultdict(int)
    for i in s:
        if i.isalpha():
            dic[i.lower()]+=1
    if len(dic)<26:
        print(f"Case {v+1}: Not a pangram")
    elif min(dic.values())==1:
        print(f"Case {v+1}: Pangram!")
    elif min(dic.values())==2:
        print(f"Case {v+1}: Double pangram!!")
    elif min(dic.values())==3:
        print(f"Case {v+1}: Triple pangram!!!")