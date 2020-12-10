# 최장 증가 부분수열

# 동적 계획법 => 0.03ms
def find(l):
    dp=[1]*len(l)
    for i,v in enumerate(l):
        for j in range(i):
            if l[j]<=v:
                dp[i]=max(dp[i],1+dp[j])
    # print(dp)
    return max(dp)

# 이진 검색 => 0.01ms, 길이만 구할수 있음
import bisect as bi

def bisec(l):
    end=[]
    for i in l:
        idx=bi.bisect(end,i)
        if idx == len(end):
            end.append(i)
        else:
            end[idx]=i
        # print(end)
    return len(end)

l=[94,8,78,22,38,79,93,8,84,39]
print(find(l))
print(bisec(l))