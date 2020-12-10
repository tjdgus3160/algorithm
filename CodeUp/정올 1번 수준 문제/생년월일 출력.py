a,b=input().split('-')
result=[]
s=""
for i in range(3):
    result.append(a[i*2:i*2+2])
if b[0]=="1":
    result[0]='19'+result[0]
    s="M"
elif b[0]=="2":
    result[0]='19'+result[0]
    s="F"
elif b[0]=="3":
    result[0]='20'+result[0]
    s="M"
elif b[0]=="4":
    result[0]='20'+result[0]
    s="F"
print("%s/%s/%s %s"%(result[0],result[1],result[2],s))
