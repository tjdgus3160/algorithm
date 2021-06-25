def solution(arr):
    res = []
    for n in arr:
        tmp=bin(n)[2:]
        if '0' not in tmp:
            res.append(int('10'+tmp[1:],2))
        elif tmp[-1]=='0':
            res.append(int(tmp[:-1]+'1',2))
        else:
            k=tmp.rfind('01')
            res.append(int(tmp[:k]+'10'+tmp[k+2:],2))
    return res

arr=[2,7,9]
print(solution(arr))