a,b=map(int,input().split())
tmp=[i*b-1 for i in range(1,100)]
for i in range(a):
    if i==0 or i==a-1:
        print("*"*a)
        tmp =list(map(lambda x:x-1,tmp))
    else:
        for j in range(a):
            if j in tmp:
                print("*",end="")
            elif j==0 or j==a-1:
                print("*",end="")
            else:
                print(" ",end="")
        tmp =list(map(lambda x:x-1,tmp))
        print()
