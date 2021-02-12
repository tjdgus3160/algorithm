def solution(nums):
    a=set(nums)
    if len(a)>=len(nums)//2:
        return len(nums)//2
    return len(a)