def gcd(a,b):
    while b!=0:
        result=b
        a,b=b,a%b
    return result

a,b=map(int,input().split())
print(gcd(a,b))
