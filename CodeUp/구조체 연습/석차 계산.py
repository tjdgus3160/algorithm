input()
l=list(map(int,input().split()))
tmp=sorted(l,reverse=True)
dict={}
for i in range(len(tmp)):
    if tmp[i] not in dict:
        dict[tmp[i]]=i+1
for i in l:
    print(i,dict[i])
