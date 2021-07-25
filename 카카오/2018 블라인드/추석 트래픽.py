def check(start,end,arr):
    res=0
    for s,e in arr:
        if s<end and e>=start:
            res+=1
    return res

def solution(lines):
    res = 0
    arr=[]
    for i in lines:
        _,S,T=i.split()
        h,m,s=S.split(':')
        time=int((int(h)*3600+int(m)*60+float(s))*1000)
        T=int(float(T[:-1])*1000)
        arr.append([time-T+1,time])
    for s,e in arr:
        res=max(res,check(s,s+1000,arr),check(e,e+1000,arr))
    return res

lines=[
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
print(solution(lines))