a,b,c=map(int,input().split())
res=(a*24*60+b*60+c)-16511
print(res if res>=0 else -1)