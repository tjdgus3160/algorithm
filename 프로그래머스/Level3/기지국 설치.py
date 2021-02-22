def solution(n, stations, w):
    res = 0
    start=1
    for i in stations:
        k=i-w-start
        if k>0:
            a,b=divmod(k,1+2*w)
            if b:
                res+=1
            res+=a
        start=i+w+1
    if start<=n:
        a, b = divmod(n-start+1, 1 + 2 * w)
        if b:
            res += 1
        res += a
    return res