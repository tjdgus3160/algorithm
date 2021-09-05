import sys
input=sys.stdin.read

while True:
    s=input().rstrip()
    if not s:
        break
    res=''
    for i in s:
        if not i.isalpha():
            res+=i
            continue
        k=i.lower()
        if k in 'aiyeou':
            idx='aiyeou'.index(k)
            k='aiyeou'[(idx+3)%6]
        else:
            idx='bkxznhdcwgpvjqtsrlmf'.index(k)
            k='bkxznhdcwgpvjqtsrlmf'[(idx+10)%20]
        if i.isupper():
            k = k.upper()
        res+=k
    print(res)