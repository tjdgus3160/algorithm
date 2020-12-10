# 6588번
import sys
input=sys.stdin.readline

l=[True for _ in range(1000001)]
l[1]=False
for i in range(2,int(1000000**0.5)+1):
    if l[i]:
        j=i*2
        while j<=1000000:
            l[j]=False
            j+=i
a=[]
while True:
    n=int(input())
    if n:
        a+=[n]
    else:
        break
for i in a:
    flag=1
    for j in range(3,i,2):
        if l[j] and l[i-j]:
            sys.stdout.writelines("{} = {} + {}\n".format(i,j,i-j))
            flag=0
            break
    if flag:
        sys.stdout.writelines("Goldbach's conjecture is wrong.\n")