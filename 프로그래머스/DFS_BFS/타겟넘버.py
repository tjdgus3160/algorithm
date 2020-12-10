def solution(arr, target):
    l=[0]
    for i in arr:
        for j in range(len(l)):
            t=l[j]
            l[j]-=i
            l.append(t+i)
    return l.count(target)

arr=[1,1,1,1,1]
t=3
print(solution(arr,t))

# 재귀
def solution(arr,target):
    if not arr and target==0: # 배열이 없고 타겟이 0일때, 타겟을 만든 것 1리턴
        return 1
    elif not arr:   # 배열이 없을 때, 더이상 타겟을 못만듬 0 리턴
        return 0
    else:
        return solution(arr[1:],target-arr[0])+solution(arr[1:],target+arr[0])