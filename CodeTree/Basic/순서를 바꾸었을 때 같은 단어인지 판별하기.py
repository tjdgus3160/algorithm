from collections import Counter

a=input().rstrip()
b=input().rstrip()
print('Yes' if Counter(a)==Counter(b) else 'No')