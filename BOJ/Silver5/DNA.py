# 1969번
n,m=map(int,input().split())
s=list("ACGT")
dict={'A':0,'C':0,'G':0,'T':0}
DNA=[input() for _ in range(n)]
result=""
cnt=0
for i in range(m):
    for j in range(n):
        dict[DNA[j][i]]+=1
    tmp = sorted(dict.items(), key=lambda x:(-x[1],x[0]))
    result+=tmp[0][0]
    cnt+=n-tmp[0][1]
    for k in s:
        dict[k]=0
print(result)
print(cnt)