# 10610번
s=input()
l=sorted(list(map(int,list(s))),reverse=True)
if 0 not in l or sum(l)%3 != 0:
    print(-1)
else:
    print("".join(list(map(str,l))))