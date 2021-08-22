def solution(N, number):
    res = -1
    dp=[]
    for i in range(1,9):
        tmp=set()
        tmp.add(int(str(N)*i))
        for j in range(i-1):
            for a in dp[j]:
                for b in dp[-j-1]:
                    tmp.add(a+b)
                    tmp.add(a-b)
                    tmp.add(a*b)
                    if b:
                        tmp.add(a//b)
        if number in tmp:
            res=i
            break
        dp.append(tmp)
    return res