def func(s):
    cnt=0
    arr=[]
    for i in s:
        if len(arr)>1 and arr[-1]=='1' and arr[-2]=='1' and i=='0':
            arr.pop()
            arr.pop()
            cnt+=1
        else:
            arr.append(i)
    k=0
    for idx,v in enumerate(arr):
        if v=='1' and (idx==len(arr)-1 or arr[idx+1]=='1'):
            break
        k+=1
    return ''.join(arr[:k]+['110'*cnt]+arr[k:])

def solution(s):
    return [func(i) for i in s]

s=["1110","100111100","0111111010"]
print(solution(s))