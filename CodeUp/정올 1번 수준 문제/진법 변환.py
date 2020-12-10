import sys
input=sys.stdin.readline

n=int(input())
print(2,bin(n)[2:])
print(8,oct(n)[2:])
print(16,hex(n)[2:].upper())
