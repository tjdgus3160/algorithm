import sys
input=sys.stdin.readline

s=input().rstrip()
n=0
cnt=0
cur=None
for i in s:
    if not cur:
        if i!='w':
            print(0)
            exit()
        cur=i
        n=1
    else:
        if cur==i:
            if i=='w':
                n+=1
            else:
                cnt+=1
                if cnt>n:
                    print(0)
                    exit()
        else:
            k='wolf'[('wolf'.index(cur)+1)%4]
            if k!=i:
                print(0)
                exit()
            if cur!='w' and cnt!=n:
                print(0)
                exit()
            if k=='w':
                n=1
            else:
                cnt=1
            cur = k
if cur!='f' or cnt!=n:
    print(0)
    exit()
print(1)
