from collections import defaultdict

def solution(strs, t):
    dp=[float('inf')]*len(t)
    dic=defaultdict(list)
    for i in strs:
        dic[i[-1]].append(i)
    if t[0] in dic[t[0]]:
        dp[0]=1
    for i in range(1,len(t)):
        for j in dic[t[i]]:
            if j==t[i-len(j)+1:i+1]:
                if len(j)==(i+1):
                    dp[i]=1
                elif len(j)<(i+1):
                    dp[i]=min(dp[i],dp[i-len(j)]+1)
    return dp[-1] if dp[-1] != float('inf') else -1

strs=["ba","na","n","a"]
t="b"
print(solution(strs,t))