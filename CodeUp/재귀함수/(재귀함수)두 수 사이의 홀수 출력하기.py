def find(a,b):
    if a>b:
        return
    if a%2==1:
        print(a,end=" ")
        find(a+2,b)
    else:
        find(a+1,b)

a,b=map(int,input().split())
find(a,b)
