tmp=[]
for i in range(int(input())):
    tmp.append(input().split())
tmp.sort(key=lambda x:int(x[1]),reverse=True)
t=tmp[0]
res=[tmp[0][0]]
res.append(sum([1 for i in tmp if int(i[2])>int(t[2])])+1)
res.append(sum([1 for i in tmp if int(i[3])>int(t[3])])+1)
print(*res)

