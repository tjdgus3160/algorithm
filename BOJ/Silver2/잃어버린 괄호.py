# 1541번
s=input()
flag=False
l=[]
tmp=0
for i in s:
    if i.isdigit():
        tmp=tmp*10+int(i)
    else:
        l.append(str(tmp))
        l.append(i)
        tmp=0
l.append(str(tmp))
s="".join(l)
i=0
while True:
    if i == len(s):
        break
    if s[i]=='-':
        if not flag:
            s=s[:i+1]+'('+s[i+1:]
            flag=True
            i+=1
        else:
            s = s[:i] + ')' + s[i:]
            flag=False
    i+=1
if flag:
    s=s+')'
print(eval(s))
