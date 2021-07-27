def solution(begin, end):
    res=[1]*(end-begin+1)
    if begin==1:
        res[0]=0
    for i in range(begin,end+1):
        for j in range(2,int(i**0.5)+1):
            if i%j==0 and i//j<=10000000:
                res[i-begin]=i//j
                break
    return res

start=1000000
end=1000200
print(solution(start,end))