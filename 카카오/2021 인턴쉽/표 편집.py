N=20
dat=[-1]*N
pre=[-1]*N
nxt=[-1]*N

def traverse():
    cur=nxt[0]
    while cur!=-1:
        print(dat[cur],end=' ')
        cur=nxt[cur]
    print()

def insert(idx,v): # idx번째 요소 뒤에 v 삽입
    dat[v+1]=v # 새로운 원소 생성
    pre[v+1]=idx # 삽입할 위치의 주소 대입
    nxt[v+1]=nxt[idx] # 삽입할 위치의 nxt값 대입
    if nxt[idx]!=-1:
        pre[nxt[idx]]=v+1
    nxt[idx]=v+1

def erase(idx):
    nxt[pre[idx]]=nxt[idx]
    if nxt[idx]!=-1:
        pre[nxt[idx]]=pre[idx]

def rollback(idx):
    nxt[pre[idx]]=idx
    pre[nxt[idx]]=idx

def solution(n, k, cmd):
    for i in range(n):
        insert(i,i)
    clear=[]
    k+=1
    for i in cmd:
        a,*tmp=i.split()
        if a=='U':
            for _ in range(int(tmp[0])):
                k=pre[k]
        elif a=='D':
            for _ in range(int(tmp[0])):
                k=nxt[k]
        elif a=='C':
            clear.append(k)
            if nxt[k]==-1:
                k=pre[k]
                erase(nxt[k])
            else:
                k=nxt[k]
                erase(pre[k])
        else:
            idx=clear.pop()
            rollback(idx)
    res = ['X'] *n
    cur = nxt[0]
    while cur != -1:
        res[dat[cur]]='O'
        cur = nxt[cur]
    return ''.join(res)

n=8
k=0
cmd=["C","C","C","Z","Z"]
print(solution(n,k,cmd))