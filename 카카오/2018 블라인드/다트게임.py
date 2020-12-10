# 10이란 숫자를 파악 할 때 조건 주의

input=["1S2D*3T","1D2S#10S","1D2S0T","1S*2T*3S","1D#2S*3S","1T2D3D#","1D2S3T*"]
output=[37,9,3,23,5,-4,59]

def find(s):
    bonus="SDT"
    n=[]
    for i in range(len(s)):
        if s[i] in bonus:
            n.append(n.pop()**(bonus.index(s[i])+1))
        elif s[i] == '0' and s[i-1] == '1':
            continue
        elif s[i] in "*":
            t1=n.pop()*2
            if len(n) != 0:
                t2=n.pop()*2
                n.append(t2)
            n.append(t1)
        elif s[i] in "#":
            n.append(n.pop()*(-1))
        else:
            tmp=int(s[i])
            if s[i+1]=='0':
                tmp=10
            n.append(tmp)
    return sum(n)

print(find("1T2D3D#"))