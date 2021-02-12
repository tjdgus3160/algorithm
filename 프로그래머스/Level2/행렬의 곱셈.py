def solution(arr1, arr2):
    res=[]
    for i in arr1:
        tmp=[]
        for sub in zip(*arr2):
            k=sum([i[j]*sub[j] for j in range(len(i))])
            tmp.append(k)
        res.append(tmp)
    return res