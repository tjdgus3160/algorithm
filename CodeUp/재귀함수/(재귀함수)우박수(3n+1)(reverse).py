def find(n):
    if n==1:
        print(1)
        return
    if n%2==1:
        find(3*n+1)
    else:
        find(n//2)
    print(n)

n=int(input())
find(n)
