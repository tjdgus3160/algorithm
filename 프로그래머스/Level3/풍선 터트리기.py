# 양쪽다 작은 경우만 제외하면 됨으로 양쪽에서부터 시작하여 작은수 발견시 갱신
def solution(a):
    res=2
    left=a[0]
    right=a[-1]
    for i in range(1,len(a)-1):
        if a[i]<left:
            left=a[i]
            res+=1
        if a[-1-i]<right:
            right=a[-1-i]
            res+=1
    return res if left!=right else res-1

a=[-16,27,65,-2,58,-92,-71,-68,-61,-33]
print(solution(a))