# 3518번
import sys
input=sys.stdin.readline

line=[]
weigh=[]
while True:
    s=input().rstrip('\n')
    if not s:
        break
    tmp=s.split()
    line.append(tmp)
    for i in range(len(tmp)):
        if len(weigh)<i+1:
            weigh.append(len(tmp[i]))
        else:
            if weigh[i]<len(tmp[i]):
                weigh[i]=len(tmp[i])

for i in line:
    res=""
    for j in range(len(i)):
        res+=(i[j]+' '*(weigh[j]-len(i[j])))
        res+=' '
    print(res.rstrip())


