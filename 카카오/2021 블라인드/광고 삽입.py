def decode(s):
    H,M,S=map(int,s.split(':'))
    return H*3600+M*60+S
def encode(n):
    H,M,S=n//3600,n//60%60,n%60
    return ("%02d:%02d:%02d"%(H,M,S))

def solution(play_time, adv_time, logs):
    play_time=decode(play_time)
    adv_time=decode(adv_time)
    weights=[0]*(play_time+1)
    for log in logs:
        s,e=map(decode,log.split('-'))
        weights[s]+=1
        weights[e]-=1
    for i in range(1,play_time+1):
        weights[i]+=weights[i-1]
    res=0
    k=sum(weights[:adv_time])
    tmp=k
    for i in range(1,play_time-adv_time+1):
        k=k-weights[i-1]+weights[i+adv_time-1]
        if k>tmp:
            tmp=k
            res=i
    return encode(res)