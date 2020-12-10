def find(n):
    if n==1:
        print(1)
        return
    print(n)
    if n%2==1:
        find(3*n+1)
    else:
        find(n//2)

n=int(input())
find(n)
