# 1063번
import sys
input=sys.stdin.readline

def move(loc,cmd):
    x,y=list(loc)
    res=True
    for c in cmd:
        if c=="R":
            if x=='H':
                res=False
            x=chr(ord(x)+1)
        elif c=="L":
            if x=='A':
                res=False
            x=chr(ord(x)-1)
        elif c=="B":
            if y=='1':
                res=False
            y=str(int(y)-1)
        elif c=="T":
            if y=='8':
                res=False
            y=str(int(y)+1)
    return res,"".join([x,y])


king,stone,n=input().split()
for _ in range(int(n)):
    c=input()
    tmpstone=""
    res,tmpking=move(king,c)
    if res:
        if tmpking==stone:
            res1, tmpstone = move(stone, c)
            if res1:
                king = tmpking
                stone=tmpstone
        else:
            king=tmpking
print(king,stone)