def find(n):
    if n==1:
        print("*")
        return
    find(n-1)
    print("*"*n)

n=int(input())
find(n)
