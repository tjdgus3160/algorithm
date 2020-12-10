def find(n):
    if n<2:
        print(n,end="")
        return
    find(n//2)
    print(n%2,end="")

n=int(input())
find(n)
