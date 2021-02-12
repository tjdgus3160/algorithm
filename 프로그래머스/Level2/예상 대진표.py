def solution(n,a,b):
    res = 0
    arr=[*range(1,n+1)]
    flag=True
    while flag:
        tmp=[]
        res+=1
        for i in range(0,len(arr),2):
            if (arr[i]==a and arr[i+1]==b) or (arr[i]==b and arr[i+1]==a):
                flag=False
                break
            if arr[i+1]==a or arr[i+1]==b:
                tmp.append(arr[i+1])
            else:
                tmp.append(arr[i])
        arr=tmp
    return res