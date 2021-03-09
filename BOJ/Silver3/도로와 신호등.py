# 2980번
import sys
input=sys.stdin.readline

n,l=map(int,input().split())
arr=[]
dic={}
for _ in range(n):
    d,r,g=map(int,input().split())
    dic[d]={'r':r,'g':g,'cur':0,'s':'R'}
time=0
loc=0
while True:
    if loc==l:
        break
    if (loc not in dic) or (loc in dic and dic[loc]['s']=='G'):
        loc+=1
    for i in dic.values():
        i['cur']+=1
        if i['s']=='R' and i['cur']==i['r']:
            i['cur']=0
            i['s']='G'
        elif i['s']=='G' and i['cur']==i['g']:
            i['cur']=0
            i['s']='R'
    time+=1
print(time)