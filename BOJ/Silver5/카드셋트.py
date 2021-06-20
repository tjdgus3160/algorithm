# 11507번
import sys
input=sys.stdin.readline

s=input().rstrip()
arr={'P':set(),'K':set(),'H':set(),'T':set()}
alp,num='',''
for i in s:
    if i.isalpha():
        if alp:
            if num in arr[alp]:
                print('GRESKA')
                exit()
            arr[alp].add(num)
            num = ''
        alp=i
    else:
        num+=i
if num in arr[alp]:
    print('GRESKA')
    exit()
arr[alp].add(num)
print(*[13-len(arr[i]) for i in arr])