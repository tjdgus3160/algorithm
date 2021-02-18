# 1991번
import sys
input=sys.stdin.readline

def perorder(root):
    print(root,end='')
    if dic[root] and dic[root][0]!='.':
        perorder(dic[root][0])
    if dic[root] and dic[root][1]!='.':
        perorder(dic[root][1])

def inorder(root):
    if dic[root] and dic[root][0]!='.':
        inorder(dic[root][0])
    print(root,end='')
    if dic[root] and dic[root][1]!='.':
        inorder(dic[root][1])

def postorder(root):
    if dic[root] and dic[root][0]!='.':
        postorder(dic[root][0])
    if dic[root] and dic[root][1]!='.':
        postorder(dic[root][1])
    print(root,end='')

n=int(input())
dic={}
for _ in range(n):
    a,b,c=input().split()
    dic.setdefault(a,[])
    dic[a].append(b)
    dic[a].append(c)
perorder('A')
print()
inorder('A')
print()
postorder('A')