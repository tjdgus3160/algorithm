n,m=map(int,input().split())
dict=[]
for _ in range(n):
    a,b=input().split()
    b=int(b)
    dict.append([a,b])
l=sorted(dict,key=lambda x:x[1],reverse=True)
for i in range(m):
    print(l[i][0])
