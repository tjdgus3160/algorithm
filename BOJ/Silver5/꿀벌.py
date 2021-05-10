# 9733번
import sys
input=sys.stdin.readline

dic={'Re':0,'Pt':0,'Cc':0,'Ea':0,'Tb':0,'Cm':0,'Ex':0}

n=0
while True:
    s=input().rstrip()
    if not s:
        break
    for i in s.split():
        n+=1
        if i in dic:
            dic[i]+=1
for key,value in dic.items():
    print('%s %d %.2f'%(key,value,round(value/n,2)))
print(f'Total {n} 1.00')