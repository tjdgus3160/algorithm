import sys
input=sys.stdin.readline

tmp=list(input())
l=[]
cnt=0
flag=True
if tmp[-1]=="\n":
    del tmp[-1]

for i in tmp:
    if i in "([":
        l.append(i)
    else:
        t=0
        while True:
            if not l:
                flag=False
                break
            k=l.pop()
            if i==')' and k=="(":
                if t>0:
                    l.append(str(2*t))
                else:
                    l.append('2')
                break
            elif i==']' and k=="[":
                if t>0:
                    l.append(str(3*t))
                else:
                    l.append('3')
                break
            elif k.isdigit():
                t+=int(k)
            else:
                flag=False
                break
if flag:
    try:
        print(sum(map(int,l)))
    except:
        print(0)
else:
    print(0)
